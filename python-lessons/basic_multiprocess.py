import multiprocessing
import time

def audit_branch_roaster(branch_name, duration):
    """" simulates running an automated  audit  on a branch roaster
    """

    print(f"{branch_name} Starting  roaster audit")
    time.sleep(duration)
    print(f"{branch_name} Audit completed!")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=audit_branch_roaster, args=("Branch_Alpha", 2))
    p2 = multiprocessing.Process(target=audit_branch_roaster, args=("Branch_Beta", 1))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("All branch roaster diagnostics complete")
