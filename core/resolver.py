import importlib
import random
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

class ResolverScript:
  def __init__(self):
    pass

  @staticmethod
  def __convert_to_class_name(file_name):
    words = file_name.split("_")
    capitalized_words = [word.capitalize() for word in words]
    return "".join(capitalized_words)

  @staticmethod
  def getScript(file_name: str) -> types.Script:
    path = ResolverPath.resolve(f"@scripts/{file_name}.py")
    class_name = ResolverScript.__convert_to_class_name(file_name)

    try:
        spec = importlib.util.spec_from_file_location(file_name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        script_class = getattr(module, class_name)
    except ImportError:
        raise ImportError(f"Não foi possível importar o módulo {class_name} de {path}.")
    except AttributeError:
        raise AttributeError(f"A classe {class_name} não foi encontrada no módulo {path}.")
    return script_class()

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