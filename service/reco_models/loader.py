import os
import pickle

import service.reco_models.userknn


class Unpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if name == "UserKnn":
            user_KNN = service.reco_models.userknn.UserKnn
            return user_KNN

        return super().find_class(module, name)


def load(path: str):
    with open(os.path.join(path), "rb") as f:
        return Unpickler(f).load()
