import featuretools as ft


def load_full_entityset(cyber_df):
    es = ft.EntitySet("CyberLL")
    # create an index column
    cyber_df["name_host_pair"] = cyber_df["src_name"].str.cat(
                                    [cyber_df["dest_name"],
                                     cyber_df["src_host"],
                                     cyber_df["dest_host"]],
                                    sep=' / ')
    cyber_df["src_pair"] = cyber_df["src_name"].str.cat(
                                     cyber_df["src_host"],
                                     sep=' / ')
    cyber_df["dest_pair"] = cyber_df["dest_name"].str.cat(
                                     cyber_df["dest_host"],
                                     sep=' / ')
    es.entity_from_dataframe("log",
                             cyber_df,
                             index="log_id",
                             time_index="secs")
    es.normalize_entity(base_entity_id="log",
                        new_entity_id="name_host_pairs",
                        index="name_host_pair",
                        additional_variables=["src_name", "dest_name",
                                              "src_host", "dest_host",
                                              "src_pair",
                                              "dest_pair",
                                              "label"])
    es.normalize_entity(base_entity_id="name_host_pairs",
                        new_entity_id="src_pairs",
                        index="src_pair",
                        additional_variables=["src_name", "src_host"])
    es.normalize_entity(base_entity_id="src_pairs",
                        new_entity_id="src_names",
                        index="src_name")
    es.normalize_entity(base_entity_id="src_pairs",
                        new_entity_id="src_hosts",
                        index="src_host")
    es.normalize_entity(base_entity_id="name_host_pairs",
                        new_entity_id="dest_pairs",
                        index="dest_pair",
                        additional_variables=["dest_name", "dest_host"])
    es.normalize_entity(base_entity_id="dest_pairs",
                        new_entity_id="dest_names",
                        index="dest_name")
    es.normalize_entity(base_entity_id="dest_pairs",
                        new_entity_id="dest_hosts",
                        index="dest_host")
    return es


def generate_cutoffs(cyber_df, index_col, after_n_obs):
    grouped = cyber_df.groupby(index_col)[index_col].count()
    grouped.name = "count"
    enough_examples = grouped[grouped > after_n_obs].to_frame().reset_index()
    enough_examples = cyber_df[cyber_df[index_col].isin(enough_examples[index_col])]
    cutoffs = enough_examples.groupby(index_col)[[index_col, "secs"]].apply(lambda x: x.iloc[after_n_obs])
    return cutoffs
