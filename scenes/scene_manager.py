import sys

sys.path.append("..")

import scenes

def load_scene(scene_name, args=None):
    # match(scene_name):
    #     case "card_list":
    #         scenes.card_list.load_scene()

    module = getattr(scenes, scene_name)
    if not args:
        module.load_scene()
    else:
        module.load_scene(*args)