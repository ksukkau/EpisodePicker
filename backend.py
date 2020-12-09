import pandas
import random

#select a series
def series_random():
    df=pandas.read_csv("StarTrekEpisodes3.csv")
    series=df["Series"]
    s=random.choice(series)
    return s

def episode_picker():
    df=pandas.read_csv("StarTrekEpisodes3.csv")
    series=df["Series"]
    s=series_random()
    indices = [i for i, x in enumerate(series) if x == s]
    rand_index=random.choice(indices)
    return rand_index

def episode():
    df = pandas.read_csv("StarTrekEpisodes3.csv")
    info = df.iloc[episode_picker(),1:5]
    return info

def TOS():
    df = pandas.read_csv("StarTrekEpisodes3.csv")
    series = df["Series"]
    s = "TOS"
    indices = [i for i, x in enumerate(series) if x == s]
    rand_index = random.choice(indices)
    info = df.iloc[rand_index, 1:5]
    return info

def TNG():
    df = pandas.read_csv("StarTrekEpisodes3.csv")
    series = df["Series"]
    s = "TNG"
    indices = [i for i, x in enumerate(series) if x == s]
    rand_index = random.choice(indices)
    info = df.iloc[rand_index, 1:5]
    return info

def VOY():
    df = pandas.read_csv("StarTrekEpisodes3.csv")
    series = df["Series"]
    s = "VOY"
    indices = [i for i, x in enumerate(series) if x == s]
    rand_index = random.choice(indices)
    info = df.iloc[rand_index, 1:5]
    return info

def DIS():
    df = pandas.read_csv("StarTrekEpisodes3.csv")
    series = df["Series"]
    s = "DIS"
    indices = [i for i, x in enumerate(series) if x == s]
    rand_index = random.choice(indices)
    info = df.iloc[rand_index, 1:5]
    return info

def TAS():
    df = pandas.read_csv("StarTrekEpisodes3.csv")
    series = df["Series"]
    s = "TAS"
    indices = [i for i, x in enumerate(series) if x == s]
    rand_index = random.choice(indices)
    info = df.iloc[rand_index, 1:5]
    return info

def DS9():
    df = pandas.read_csv("StarTrekEpisodes3.csv")
    series = df["Series"]
    s = "DS9"
    indices = [i for i, x in enumerate(series) if x == s]
    rand_index = random.choice(indices)
    info = df.iloc[rand_index, 1:5]
    return info

def ENT():
    df = pandas.read_csv("StarTrekEpisodes3.csv")
    series = df["Series"]
    s = "ENT"
    indices = [i for i, x in enumerate(series) if x == s]
    rand_index = random.choice(indices)
    info = df.iloc[rand_index, 1:5]
    return info

def PIC():
    df = pandas.read_csv("StarTrekEpisodes3.csv")
    series = df["Series"]
    s = "PIC"
    indices = [i for i, x in enumerate(series) if x == s]
    rand_index = random.choice(indices)
    info = df.iloc[rand_index, 1:5]
    return info



'''def episode_test():
    df = pandas.read_csv("StarTrekEpisodes.csv")
    info = df.iloc[test(),1:5]
    return info'''




#print(series_random())
#print(episode_picker())
#print(episode_test())

#print(test())