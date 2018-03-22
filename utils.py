from random import randint
import pandas as pd
def new_labels(data, labels):
    ct_ids = []
    ct_times = []
    ct_labels = []
    data = data.copy()
    data['RUL'] = labels
    gb = data.groupby(['engine_no'])
    for engine_no_df in gb:
        instances = engine_no_df[1].shape[0]
        r = randint(5, instances - 1)
        ct_ids.append(engine_no_df[1].iloc[r,:]['engine_no'])
        ct_times.append(engine_no_df[1].iloc[r,:]['time'])
        ct_labels.append(engine_no_df[1].iloc[r,:]['RUL'])
    ct = pd.DataFrame({'engine_no': ct_ids,
                       'cutoff_time': ct_times,
                       'RUL': ct_labels})
    ct = ct[['engine_no', 'cutoff_time', 'RUL']]
    ct.index = ct['engine_no']
    return ct

def make_cutoff_times(data):
    data['time'] = pd.date_range('1/1/2000', periods=data.shape[0], freq='s')

    gb = data.groupby(['engine_no'])
    labels = []


    for engine_no_df in gb:
        instances = engine_no_df[1].shape[0]
        label = [instances - i - 1 for i in range(instances)]
        labels += label
    
    return new_labels(data, labels)

def feature_importances(X, reg, feats=5):
    feature_imps = [(imp, X.columns[i]) 
                    for i, imp in enumerate(reg.feature_importances_)]
    feature_imps.sort()
    feature_imps.reverse()
    for i, f in enumerate(feature_imps[0:feats]):
        print('{}: {} [{:.3f}]'.format(i + 1, f[1], f[0]))
    print('-----\n')
    return [f[1] for f in feature_imps[:feats]]