from courses import update_courses_catalog
from cleanup import clean_pycache
import os

project_root = os.path.dirname(os.path.abspath(__file__))

print("Updating courses catalog...")
update_courses_catalog()
print("Courses catalog updated successfully.")

print("Cleaning up __pycache__ directories...")
clean_pycache(project_root)
print("Cleanup completed successfully.")