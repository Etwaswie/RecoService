# type: ignore
# pylint: disable-all

import os
import pickle

from service.api.recommenders import top_popular

lightfm_ann = None
MODEL_PATH = "service/reco_models/LF_model.pkl"
if os.path.exists(MODEL_PATH):
    lightfm_ann = pickle.load(open(MODEL_PATH, "rb"))

popular_recos = top_popular(k=10)


def get_recos_lightfm_ann(user_id, k_recs=10):
    if user_id in lightfm_ann.user_id_map.external_ids:  # type: ignore
        return lightfm_ann.get_item_list_for_user(user_id, top_n=k_recs).tolist()  # type: ignore
    else:
        return popular_recos[:10]
