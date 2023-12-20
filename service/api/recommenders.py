# type: ignore

import random

import pandas as pd

top_20 = pd.read_csv("data/top_20_items.csv")
top_weight_duration = pd.read_csv("data/top_weight_items.csv")
top_items = pd.read_csv("data/top_items.csv")
viewed_films = pd.read_csv("data/viewed_films.csv")

top_items_list = top_items.sort_values("views", ascending=False)["item_id"].to_list()


def top_popular(k):
    reco = top_20["item_id"].head(k).to_list()
    return reco


def weighted_random_recommendation(n, items_weights=top_weight_duration):
    reco = random.choices(items_weights["item_id"], items_weights["weight"], k=n)
    return reco


def top_popular_without_viewed(user_id, k):
    top = top_items_list
    if len(viewed_films[viewed_films["user_id"] == user_id]["items_list_id"].to_list()) > 0:
        viewed_films_user = viewed_films[viewed_films["user_id"] == user_id]["items_list_id"].to_list()[0]
    else:
        viewed_films_user = []

    for i in enumerate(viewed_films_user):
        if viewed_films_user[i[0]] in top:
            top.remove(viewed_films_user[i[0]])

    reco = top_items_list[:k]
    return reco


dssm_reco_path = "data/reco_dssm1.csv"
dssm_recos = pd.read_csv(dssm_reco_path, sep=";")

users_dssm = dssm_recos["user_id"].unique()
dssm_recos["item_id"] = dssm_recos["item_id"].apply(
    lambda x: list(map(int, x.replace("'", "").replace("[", "").replace("]", "").split(", ")))
)

MV_reco_path = "data/reco_recbole.csv"
MV_recos = pd.read_csv(MV_reco_path, sep=";")

users_MV = MV_recos["user_id"].unique()
MV_recos["item_id"] = MV_recos["item_id"].apply(
    lambda x: list(map(int, x.replace("'", "").replace("[", "").replace("]", "").split(", ")))
)


def dssm_offline_reco(user_id):
    if user_id in users_dssm:
        user_recos = dssm_recos[dssm_recos["user_id"] == user_id]["item_id"].to_list()[0]
        return user_recos
    return top_popular(10)


def mv_offline_reco(user_id):
    if user_id in users_MV:
        user_recos = MV_recos[MV_recos["user_id"] == user_id]["item_id"].to_list()[0]
        return user_recos
    return top_popular(10)


rank_reco_path = 'data/reco_ranker.csv'
rank_recos = pd.read_csv(rank_reco_path, sep = ';')

users_ranker = rank_recos['user_id'].unique()
rank_recos['item_id'] = (rank_recos['item_id']
                         .apply(lambda x: list(map(int, x
                                                   .replace("'", "")
                                                   .replace("[", "")
                                                   .replace("]", "")
                                                   .split(", ")))))


def ranker_offline_reco(user_id):
    if user_id in users_ranker:
        user_recos = rank_recos[rank_recos['user_id'] == user_id]['item_id'].to_list()[0]
        return user_recos
    return top_popular(10)
