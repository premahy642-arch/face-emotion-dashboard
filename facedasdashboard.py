import sys
sys.path.append('./src')

from faceDashboard import FaceDashboard
if __name__ == "__main__":
    print("Dashboard is running...")
    dashboard = FaceDashboard()
    dashboard.run()
