import datetime
import importlib.util
import random
import threading
import yaml
import os
import core.types as types
class ResolverConfig:
  __settings: types.TSettings = None
  def __init__(self):
    pass

  @staticmethod
  def resolve() -> types.TSettings:
    if(ResolverConfig.__settings is None):
      ResolverConfig.__settings = ResolverFile.readYaml(f"{ResolverPath.getLocalPath()}/settings.yaml")
    
    return ResolverConfig.__settings
  
  @staticmethod
  def get(key: str) -> types.TSettings:
    return ResolverConfig.resolve()[key]
  
  @staticmethod
  def set(key: str, value):
    keys = key.split("/")
    settings = ResolverConfig.resolve()
    for i in range(len(keys)):
      if i == len(keys) - 1:
        settings[keys[i]] = value
      else:
        settings = settings[keys[i]]
    ResolverFile.writeYaml(f"{ResolverPath.getLocalPath()}/settings.yaml", ResolverConfig.resolve())

class ResolverVolume:
  @staticmethod
  def calcVolumeToGeneral(volume: float) -> float:
    return float(volume * ResolverConfig.resolve()["game"]["volume"]["geral"])
  @staticmethod
  def handleVolume(type: str) -> int:
    if type == "music":
      return ResolverVolume.calcVolumeToGeneral(ResolverConfig.resolve()["game"]["volume"]["music"])
    elif type == "effects":
      return ResolverVolume.calcVolumeToGeneral(ResolverConfig.resolve()["game"]["volume"]["effects"])
    else:
      raise Exception("Volume type not found")

class ResolverScript:
  def __init__(self):
    pass

  @staticmethod
  def __convert_to_class_name(file_name):
    words = file_name.split("_")
    capitalized_words = [word.capitalize() for word in words]
    return "".join(capitalized_words)

  @staticmethod
  def getScript(file_name: str, *args) -> types.Script:
    path = ResolverPath.resolve(f"@scripts/{file_name}.py")
    class_name = ResolverScript.__convert_to_class_name(file_name)
    Logger.debug("script", f"Loading {class_name} in {path}")
    try:
        spec = importlib.util.spec_from_file_location(file_name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        script_class = getattr(module, class_name)
    except ImportError:
        raise ImportError(f"Não foi possível importar o módulo {class_name} de {path}.")
    except AttributeError:
        raise AttributeError(f"A classe {class_name} não foi encontrada no módulo {path}.")
    return script_class(*args)

class ResolverCoords:
  def __init__(self, min: types.TCoord, max: types.TCoord):
    self.__min = min
    self.__max = max

  @property
  def min(self) -> types.TCoord:
    return self.__min
  
  @property
  def max(self) -> types.TCoord:
    return self.__max
  
  @property
  def size(self) -> types.TSize:
    return (self.__max[0] - self.__min[0], self.__max[1] - self.__min[1])
  
  @property
  def center(self) -> types.TCoord:
    return (self.__min[0] + self.size[0]/2, self.__min[1] + self.size[1]/2)
  
  @property
  def center_x(self) -> int:
    return self.__min[0] + self.size[0]/2
  
  @property
  def center_y(self) -> int:
    return self.__min[1] + self.size[1]/2
  
  def getRandomCoord(self) -> types.TCoord:
    return (random.randint(self.__min[0], self.__max[0]), random.randint(self.__min[1], self.__max[1]))
  
  def getRandomCoordX(self) -> int:
    return random.randint(self.__min[0], self.__max[0])
  
  def getRandomCoordY(self) -> int:
    return random.randint(self.__min[1], self.__max[1])
  

  @staticmethod
  def getCoordsWithCenter(screenSize: types.TSize, size: types.TSize) -> types.TCoord:
    return (screenSize[0]/2 - size[0]/2, screenSize[1]/2 - size[1]/2)
  
  @staticmethod
  def getCoordsWithCenterX(screenSize: types.TSize, size: types.TSize) -> types.TCoord:
    return (screenSize[0]/2 - size[0]/2, size[1])
  
  @staticmethod
  def getCoordsWithCenterY(screenSize: types.TSize, size: types.TSize) -> types.TCoord:
    return (size[0], screenSize[1]/2 - size[1]/2)

  @staticmethod
  def getSizeScreen() -> types.TSize:
    return ResolverConfig.resolve()["window"]["dimension"]

class ResolverPath:
  def __init__(self):
    pass

  @staticmethod
  def resolve(path: str):
    if path.find("@") == -1:
      return path
    paths = ResolverConfig.resolve()["paths"]
    for key in paths:
      path = path.replace(f"@{key}", paths[key])
      
    return f"{ResolverPath.getLocalPath()}/{path}"
  
  @staticmethod
  def getLocalPath():
    return os.getcwd()
    
class ResolverFile:
  def __init__(self):
    pass

  @staticmethod
  def getAllWithDir(path: str) -> "list[str]":
    return os.listdir(ResolverPath.resolve(path))
  
  @staticmethod
  def getAllFilesWithExtension(path: str, extension: str) -> "list[str]":
    files = []
    for file in ResolverFile.getAllWithDir(path):
      if file.endswith(extension):
        files.append(file)
    files.sort()
    return files
  
  @staticmethod
  def read(path: str) -> str:
    try:
      with open(ResolverPath.resolve(path), "r") as file:
        read = file.read()
        file.close()
        return read
    except:
      raise Exception("File not found or not permission")
    
  @staticmethod
  def write(path: str, content: str) -> bool:
    try:
      with open(ResolverPath.resolve(path), "w") as file:
        file.write(content)
        file.close()
      return True
    except:
      return False
    
  @staticmethod
  def append(path: str, content: str) -> bool:
    try:
      with open(ResolverPath.resolve(path), "a") as file:
        file.write(content)
        file.close()
      return True
    except:
      return False

  @staticmethod
  def readYaml(path: str) -> dict:
    try:
      with open(ResolverPath.resolve(path), "r") as file:
        read = yaml.load(file, Loader=yaml.FullLoader)
        file.close()
        return read
    except:
      raise Exception("File not found or not permission")
    
  @staticmethod
  def writeYaml(path: str, content: dict) -> bool:
    try:
      with open(ResolverPath.resolve(path), "w") as file:
        yaml.dump(content, file)
        file.close()
      return True
    except:
      return False
    
  @staticmethod
  def appendYaml(path: str, content: dict) -> bool:
    try:
      with open(ResolverPath.resolve(path), "a") as file:
        yaml.dump(content, file)
        file.close()
      return True
    except:
      return False
    
class Logger:
  @staticmethod
  def debug(location: str, message: str):
    if ResolverConfig.resolve()["game"]["debug"] is True:
      ResolverFile.append(f"@logger/{location}.log", f"[{datetime.datetime.now()}] - {message}\n")

  @staticmethod
  def log(location: str, message: str):
    ResolverFile.append(f"@logger/{location}.log", f"[{datetime.datetime.now()}] - {message}\n")

  @staticmethod
  def error(location: str, message: str):
    ResolverFile.append(f"@logger/{location}.log", f"[{datetime.datetime.now()}] - {message}\n")
          
  @staticmethod
  def finish():
    for i in ResolverFile.getAllFilesWithExtension("@logger", ".log"):
      ResolverFile.append(f"@logger/{i}", f"[{datetime.datetime.now()}] - Game closed, finished logger\n")


class ResolverScene:
  _instance = None
  def __new__(cls, *args, **kwargs):
    if cls._instance is None:
      cls._instance = super(ResolverScene, cls).__new__(cls)
    return cls._instance
  
  def __init__(self, *args):
    if not hasattr(self, '_instanced'):
      self._instanced = True
      self.__args = args
      self.__scenes: list = []
      self.__load()
  
  def __load(self):
    for scene in ResolverFile.getAllFilesWithExtension("@scenes", ".py"):
      self.__scenes.append(ResolverScene.handleScene(scene.replace(".py", ""), *self.__args))
  
  def isExist(self, name: str) -> bool:
    class_name = ResolverScene.__convert_to_class_name(name)
    for scene in self.__scenes:
      if scene.__class__.__name__ == class_name:
        return True
    return False

  def getByName(self, name: str) -> types.Scene:
    class_name = ResolverScene.__convert_to_class_name(name)
    for scene in self.__scenes:
      if scene.__class__.__name__ == class_name:
        return scene
    raise Exception(f"Scene {class_name} not found")
  
  def rebuild(self, name: str) -> bool:
    class_name = ResolverScene.__convert_to_class_name(name)
    for i in range(len(self.__scenes)):
      if self.__scenes[i].__class__.__name__ == class_name:
        self.__scenes[i] = ResolverScene.handleScene(name, *self.__args)
        return True
    return False

  @staticmethod
  def handleScene(name: str, *args) -> types.Scene:
    class_name = ResolverScene.__convert_to_class_name(name)
    path = ResolverPath.resolve(f"@scenes/{name}.py")
    Logger.log("sceneLoader", f"Handle Scene in {path} - {name} [{class_name}]")
    try:
      spec = importlib.util.spec_from_file_location(
        name,
        path
      )
      module = importlib.util.module_from_spec(spec)
      spec.loader.exec_module(module)
      
      return getattr(module, class_name)(*args)
    except ImportError:
      Logger.debug("sceneLoader", (f"Não foi possível importar o módulo {name} de {path}."))
    except AttributeError:
      Logger.debug("sceneLoader", (f"A classe {class_name} não foi encontrada no módulo {path}."))

  @staticmethod
  def __convert_to_class_name(file_name):
    file_name += "_scene"
    words = file_name.split("_")
    capitalized_words = [word.capitalize() for word in words]
    return "".join(capitalized_words)
  
class ManagerScenes:
  _instance = None
  def __new__(cls, *args, **kwargs):
    if ManagerScenes._instance is None:
      ManagerScenes._instance = super(ManagerScenes, cls).__new__(cls)
    return ManagerScenes._instance
  
  def __init__(self, *args):
    if not hasattr(self, '_instanced'):
      self._instanced = True
      self.__scenes_resolver = ResolverScene(*args)
      self.__historic: list[types.Scene] = []
      self.__current_scene = None

  @property
  def current_scene(self) -> str:
    return self.__current_scene
  
  def setCurrent(self, scene: types.Scene):
    self.__current_scene = scene

  @staticmethod
  def __start_scene_safely(scene: types.Scene, *data):
    try:
      scene.start(*data)
    except Exception as e:
      Logger.debug("sceneLoader", f"Scene {scene} error on start -> {e}")

  def goTo(self, name: str, *data):
    if self.__scenes_resolver.isExist(name):
      old = self.__current_scene
      self.__current_scene = self.__scenes_resolver.getByName(name)
      self.__current_scene.start(*data)
      # thread = threading.Thread(target=lambda: ManagerScenes.__start_scene_safely(self.__current_scene, *data), name=self.__current_scene.__class__.__name__)
      # thread.start()
      if old is not None:
        old.stop()
        self.__historic.append(old)
        Logger.debug("sceneLoader", f"Scene {old} stopped")
      Logger.debug("sceneLoader", f"Scene {name} started")
    else:
      Logger.debug("sceneLoader", f"Scene {name} not found")
    # thread.join()

  
  def rebuild(self, name: str):
    if not self.__scenes_resolver.rebuild(name):
      Logger.debug("sceneLoader", f"Scene {name} not found")

  def reload(self, *data):
    try:
      self.__current_scene.stop()
      self.__current_scene.start(*data)
      Logger.debug("sceneLoader", f"Scene {self.__current_scene.__class__.__name__} reloaded")
    except:
      Logger.debug("sceneLoader", f"Scene {self.__current_scene.__class__.__name__} error on reload")

  def goToBack(self, *data):
    self.__historic.pop()
    self.goTo(self.__historic.pop().__class__.__name__, *data)
  
  def goToBackAndGoTo(self, name: str, *data):
    self.__historic.pop()
    self.goTo(name, *data)