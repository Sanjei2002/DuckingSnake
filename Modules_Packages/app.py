import downloader
from py_common.util import CommonUtil

# from Has_Duplicate import hasDuplicate
import sys
import os
# Add parent directory to sys.path first
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now perform imports


utilclass = CommonUtil()
print(f"imported module printing {utilclass.give_me_a_Str()}")

print(
    f"default module look up occurs in cuurent path and other predefined paths {dir()}")

downloader.RunAsync()
# hasDuplicate([10, 23, 43, 54, 23, 54])
