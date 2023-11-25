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


class ResolverCoords:
  def __init__(self):
    pass

  @staticmethod
  def getCoordsWithCenter(screenSize: types.TCoord, size: types.TSize) -> types.TCoord:
    return (screenSize[0]/2 - size[0]/2, screenSize[1]/2 - size[1]/2)
  
  @staticmethod
  def getCoordsWithCenterX(screenSize: types.TCoord, size: types.TSize) -> types.TCoord:
    return (screenSize[0]/2 - size[0]/2, size[1])
  
  @staticmethod
  def getCoordsWithCenterY(screenSize: types.TCoord, size: types.TSize) -> types.TCoord:
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