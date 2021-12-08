import os
import platform

if __name__ == '__main__':
    print(f"{os.name} - {platform.system()} - {platform.release()}")