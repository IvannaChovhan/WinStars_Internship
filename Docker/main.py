import pandas as pd
import sys


class Model:
    
    def predict(self, data):
        return data['6']**2 + data['7']

    
if __name__ == "__main__":
    
    data_file = sys.argv[1]
    data = pd.read_csv(data_file)
    
    print("Creating a model...")
    
    model = Model()
    
    print("Model created successful")
    print("Making predictions...")
    
    predictions = model.predict(data)
    
    print("Predictions made successful")
    print("Saving to prediction.csv ...")
	
	path = data_file.split('/').pop()
    pd.DataFrame(predictions, columns=['target']).to_csv('/'.join(path) + '/prediction.csv', index=False)
    
    print("Saved! Your predictions in prediction.csv")

