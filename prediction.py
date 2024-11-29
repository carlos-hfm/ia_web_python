from lib.descriptor_gen import DescriptorGen
import numpy as np
import joblib

model = joblib.load('models/oversampled_model.pkl')
desc_gen = DescriptorGen()

def prediction(molecule_smiles, model=model, desc_gen=desc_gen):
    try:
        desc = desc_gen.from_smiles(molecule_smiles)
        desc = np.array(desc).reshape(1, -1)
        pred = model.predict(desc)
        print(pred[0])
        return pred[0]
    except Exception as e:
        print(f"An error occurred: {e}")
        return 'error'
    

#print(prediction('CC1=CC2=C(C=C1)N(C3=C2CN(CC3)C)CCC4=CN=C(C=C4)C')) 