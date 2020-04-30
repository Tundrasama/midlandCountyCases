import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def PD_main():
	url = 'http://www.midlandtexas.gov/232/Health-Senior-Services'
	html = requests.get(url).content
	df_list = pd.read_html(html)
	df = df_list
	for i,df in enumerate(df_list):
		print(f"---------------------------------------DF: {i} ---------------------------------------")

		if i == 0:
			print("Total Confirmed Cases")
			dfName="Total_Confirmed_Cases.csv"
		if i == 1:
			print("Source of Exposure")
			dfName="Source_of_Exposure.csv"
			# print(df[df.columns[0:2]])

			# x_axis = df[df.columns[0]]
			# y_axis = df[df.columns[1]]
		
			# y_pos = np.arange(len(x_axis))
			# performance = [10,8,6,4]

			# plt.bar(y_pos, y_axis, align='center', alpha=0.5)
			# plt.xticks(y_pos, x_axis,rotation=45)
			# plt.ylabel('Cases')
			# plt.tight_layout()
			# plt.title(dfName.replace('_',' ').replace('.csv',''),fontsize=20)

			# plt.show()
			
		if i == 2:
			print("Gender")
			dfName="Gender.csv"
		if i == 3:
			print("Age")
			dfName="Age.csv"
		if i == 4:
			print("Patient Status")
			dfName="Patient_Status.csv"
		if i == 5:
			print("Medical Visit")
			dfName="Medical_Visit.csv"
		if i == 6:
			print("Investigation Status")
			dfName="Investigation_Status.csv"
	
		# df.to_csv(dfName,index=False)

if __name__ == "__main__":
	plt.rcParams['toolbar'] = 'None'
	PD_main()