# type: ignore

import os
import pickle


class Unpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if name == "UserKnn":
            from service.reco_models.userknn import UserKnn  # type: ignore

            return UserKnn

        return super().find_class(module, name)


def my_load(path: str):
    with open(os.path.join(path), "rb") as f:
        return Unpickler(f).load()
