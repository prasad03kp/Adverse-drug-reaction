import pickle

def process(params):

    filename = './adr_app/decision_tree_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))

    instance = [0 for i in range(15)]

    for i in range(1,int(params['count'])+1):
        instance[int(params['key' + str(i)])] = int(params['value' + str(i)])

    instance = [instance]

    a = loaded_model.predict(instance)
    if a[0] == 0:
        return "Low"
    elif a[0] == 1:
        return "Medium"
    else:
        return "High"
