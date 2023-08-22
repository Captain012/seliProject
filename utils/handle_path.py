# handle_path
from pathlib import Path
class GetPath:
    project_path = Path(__file__).parent.parent
    data_path = project_path / 'data'
    report_path = project_path / r'outFiles/reports/tmp'
    config_path = project_path / 'config'
    log_path = project_path / 'outFiles/logs'
    screeenshot_path = project_path / 'outFiles/screenshot'
    allu_rep_path = project_path / r'outFiles/reports/allu_rep'

if __name__ == '__main__':
    a = GetPath()
    print(a.screeenshot_path / '元素未找到.png')