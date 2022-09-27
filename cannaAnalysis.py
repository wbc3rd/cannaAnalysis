import math
import numpy as np
import pandas as pd
import seaborn as sns

# set the option to see full data frames
pd.set_option("display.max_rows", None, "display.max_columns", None)

df = pd.read_csv('cannaData.csv', low_memory=False)
#print(len(df))

data = df.dropna(how="all")
#print(len(data))

strain_list = []
for i in data["strain_slug"]:
        strain_list.append(i)

# remove the duplicate values
strain_set = (set(strain_list))

# remove the NaN value
strain_set.remove(np.nan)

# determine how many unique strains in data
#print("There are",len(strain_set),"strains in this dataset.")

'''print the column names
columnList  = data.columns.to_list()
columnNo1st = columnList[1:]
strList     = ', '.join(columnNo1st)
columnStrNo = strList[:-1]
print('The columns in this dataframe are', columnStrNo + '.')'''
    
# get stats for total thc on all samples

#print('Descriptive THC stats for the dataset:')
#print(data['tot_thc'].describe())

# get stats for total cbd on all samples
#print('Descriptive CBD stats for the dataset:')
#print(data['tot_cbd'].describe())

#print('Descriptive stats for THC and CBD side by side:')
#print(data[['tot_thc', 'tot_cbd']].describe())

# how many more strains contain measurements for thc than cbd?
#print("There are",data['tot_thc'].count() - data['tot_cbd'].count(), "strains without measureable CBD.")

def chemoCounts():
    '''chemoCounts find the number of sativa, indica, and hybrid strains 
    and presents the information in a bar graph'''    
    print("Chemotype Counts:")
    data['strain_cleanCategory'] = data['strain_category'].astype('category')
    data['strain_cleanCategory'] = data['strain_cleanCategory'].cat.remove_categories('None')
    print(data['strain_cleanCategory'].value_counts())
    categoryCounts = data['strain_cleanCategory'].value_counts()
    print(sns.barplot(y=categoryCounts.index, x=categoryCounts.values))

def highCBD():
    '''highCBD gets the strain names of some high cbd strains'''
    highCBD = data['strain_slug'].loc[data['tot_cbd'] > 20]
    CBD_set = (set(highCBD))
    CBD_set.remove(np.nan)
    CBDstring = ', '.join(CBD_set)
    print("Some high CBD strains are",CBDstring + '.')

def popularStrains():
    '''popularStrains lists some popular strains on Leafly'''
    popStrains = data['strain_slug'].loc[data['strain_popularity'] > .50].unique()
    popString = ', '.join(popStrains)
    print("Some popular strains are", popString, "on Leafly.")

def highTHC():
    '''highTHC lists some high THC strains from the dataset'''
    # which strains are highest in thc?
    highTHC = data['strain_slug'].loc[data['tot_thc'] > 35].unique()
    THC_set = (set(highTHC))
    THC_set.remove(np.nan)
    THCstring = ', '.join(THC_set)
    print("Some high THC strains are",THCstring)

def strainStats():
    '''strainStats gets the averages for different categories for a given strain.'''
    while True:
        strainStatsName = input('Type a strain name to find the average stats: ')
        strainStats  = data.loc[data['strain_slug'] == strainStatsName].mean()
        if np.isnan(strainStats.has_cannabs):
            if strainStatsName == "1":
                break
            else:
                print('Strain not in database: try again or press 1 to exit')
        else:
         newStrains = strainStats.drop(['has_cannabs','has_terps'])
         refinedMax = round(newStrains[2:], 2)
         print('Here are the descriptive stats for', strainStatsName + ':')
         print(refinedMax)
         break

def mostPop():
    '''mostPop returns the most popular strain on Leafly'''
    mostPopular = data['strain_slug'].loc[data['strain_popularity'] == 1.0].unique()
    stringPop = ''.join(mostPopular)
    popTHC = data['tot_thc'].loc[data['strain_slug'] == stringPop].mean()
    refined = round(popTHC, 2)
    print('The most popular strain on leafly is',stringPop,'with a THC content of',refined)

def domTerp(): 
    '''domTerp lists some strains that have a dominant specific terpine'''
    # get strains that have a dominant terpine content
    #domTerpInp    = input("Enter a terpine: ")
    #domTerpStrain = set(data['strain_slug'].loc[data['top_terp_f'] == domTerpInp])
    #remove the nan values
    #domTerpStrain.remove(np.nan)
    #stringDom = ', '.join(domTerpStrain)
    #print("Some strains with ", domTerpInp, "are:")
    #print(stringDom)

def maxTHC():
    '''maxTHC gets the maximum THC content observed for a given strain'''
    while True:
        strainMax = input('Type a strain name to find the maximum THC content: ')
        strainMaxTHC  = data['tot_thc'].loc[data['strain_slug'] == strainMax].max()
        if np.isnan(strainMaxTHC):
            if strainMax == "1":
                break
            else:
                print('Strain not in database: try again or press 1 to exit')
        else:
         refinedMax = round(strainMaxTHC, 2)
         print(strainMax,'has a maximum THC content of',str(refinedMax) +'%')
         break

def noSamples():
    '''noSamples counts the number of samples for a given strain'''
    while True:
        strainCo     = input('Type a strain name to find the number of DB samples: ')
        strainCount  = data['strain_slug'].loc[data['strain_slug'] == strainCo].count()
        if strainCount == 0:
            if strainCo == "1":
                break
            else:
                print('Strain not in database: try again or press 1 to exit')
        else:
         print(strainCo,'has', strainCount, 'samples in this database.')
         break

def sampRegion():
    '''sampRegion shows the number of samples each region contributed to the DB'''
    print('The number of samples by region is: ')
    print(data['region'].value_counts()) # cannabis samples each region

    sampleRegionCounts = data['region'].value_counts()
    print(sns.barplot(y=sampleRegionCounts.index, x=sampleRegionCounts.values))

def avgTHC():
    '''avgTHC finds the average THC content for a given strain''' 
    while True:
        strainMean = input('Type a strain name to find the average THC content: ')
        strainTHC  = data['tot_thc'].loc[data['strain_slug'] == strainMean].mean()
        if np.isnan(strainTHC):
            if strainMean == "1":
                break
            else:
                print('Strain not in database: try again or press 1 to exit')
        else:
         refined = round(strainTHC, 2)
         print(strainMean,'has an average THC content of',refined,'%')
         break

def cannRatio():
    '''cannRatio gets the ratio of cannabinoids for a strain'''
    while True:
        strainName = input('Type a strain name to find the average THC/CBD ratio: ')
        strainTHC   = data['tot_thc'].loc[data['strain_slug'] == strainName].mean()
        strainCBD   = data['tot_cbd'].loc[data['strain_slug'] == strainName].mean()
        if np.isnan(strainTHC) or np.isnan(strainCBD):
            if strainName == "1":
                break
            else:
                print('Strain not in database: try again or press 1 to exit')
        else:
            cleanTHC = int(round(strainTHC, 2))
            cleanCBD = int(round(strainCBD, 2))
            divided     = math.gcd(cleanTHC, cleanCBD)
            strainRatio = f"{cleanTHC/divided}:{cleanCBD/divided}"
            print(strainName, 'has a ratio of', strainRatio, 'THC to CBD')
            break
 
def domTerpSearch():
    '''domTerpSearch finds the dominant terpine for a given strain'''        
    while True:
        strainTerpName = input('Type a strain name to find the dominant terpine: ')
        strainTerp     = data['top_terp_f'].loc[data['strain_slug'] == strainTerpName].value_counts().nlargest(1)
        if strainTerp.size == 0:
            if strainTerpName == "1":
                break
            else:
                print('Strain not in database: try again or press 1 to exit')
        else:
             #print(strainMean,'has an average THC content of',refined,'%')
             terpString = strainTerp.index[0]
             print("The dominant terpine for", strainTerpName, "is", terpString + ".")
             break

# use the info from this code for the machine learning pipeline
# the top 10 strains with the most samples in the dataset
#mostStrains = data['strain_slug'].value_counts().nlargest(10)
#print(mostStrains)

def firstPipe():
    '''firstPipe runs through a few of the functions to make sure they work'''
    highCBD()
    print('\n')
    popularStrains()
    print('\n')
    domTerpSearch()
    print('\n')
    maxTHC()
    
firstPipe()