# run
import pytest
import os
from utils.handle_path import GetPath
pytest.main(['-vs','--alluredir',GetPath.report_path,'--clean-alluredir'])
os.system(f'allure serve {GetPath.report_path}')










