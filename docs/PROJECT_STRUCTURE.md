Folder PATH listing for volume D:
Volume serial number is 447A-CC6C
D:.
|   .env
|   .env.docker
|   .gitignore
|   docker-compose.yml
|   Dockerfile
|   Dockerfile.celery
|   dump.rdb
|   Pipfile
|   Pipfile.lock
|   requirements.txt
|   structure.txt
|   Untitled-3.jsonc
|   
+---docs
|       ADMIN.md
|       
+---library
|   |   manage.py
|   |   periodic_tasks.py
|   |   
|   +---.pytest_cache
|   |   |   .gitignore
|   |   |   CACHEDIR.TAG
|   |   |   README.md
|   |   |   
|   |   \---v
|   |       \---cache
|   |               lastfailed
|   |               nodeids
|   |               stepwise
|   |               
|   +---accounts
|   |   |   apps.py
|   |   |   tasks.py
|   |   |   urls.py
|   |   |   __init__.py
|   |   |   
|   |   +---admin
|   |   |   |   daily_messages.py
|   |   |   |   daily_message_limit.py
|   |   |   |   email_verification.py
|   |   |   |   user_preferences.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           daily_messages.cpython-312.pyc
|   |   |           daily_message_limit.cpython-312.pyc
|   |   |           email_verification.cpython-312.pyc
|   |   |           user_preferences.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---migrations
|   |   |   |   0001_initial.py
|   |   |   |   0002_initial.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           0001_initial.cpython-312.pyc
|   |   |           0002_initial.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---models
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   +---user
|   |   |   |   |   user_preferences.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           user_preferences.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   +---verification
|   |   |   |   |   daily_messages.py
|   |   |   |   |   daily_message_limit.py
|   |   |   |   |   email_verification.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           daily_messages.cpython-312.pyc
|   |   |   |           daily_message_limit.cpython-312.pyc
|   |   |   |           email_verification.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   \---__pycache__
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---serializers
|   |   |   |   __init.py
|   |   |   |   
|   |   |   +---auth
|   |   |   |   |   register.py
|   |   |   |   |   session_serializers.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           register.cpython-312.pyc
|   |   |   |           session_serializers.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   +---password
|   |   |   |   |   change_password.py
|   |   |   |   |   reset_password.py
|   |   |   |   |   reset_password_send_code.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           change_password.cpython-312.pyc
|   |   |   |           reset_password.cpython-312.pyc
|   |   |   |           reset_password_send_code.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   +---user
|   |   |   |   |   user.py
|   |   |   |   |   user_preferences.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           user.cpython-312.pyc
|   |   |   |           user_preferences.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   \---verification
|   |   |       |   send_verification_code.py
|   |   |       |   __init__.py
|   |   |       |   
|   |   |       \---__pycache__
|   |   |               send_verification_code.cpython-312.pyc
|   |   |               __init__.cpython-312.pyc
|   |   |               
|   |   +---tests
|   |   |   +---models
|   |   |   |   |   test_daily_messages.py
|   |   |   |   |   test_daily_message_limit.py
|   |   |   |   |   test_email_verification.py
|   |   |   |   |   test_user_preferences.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           test_daily_messages.cpython-312-pytest-8.3.4.pyc
|   |   |   |           test_daily_messages.cpython-312-pytest-8.3.5.pyc
|   |   |   |           test_daily_message_limit.cpython-312-pytest-8.3.4.pyc
|   |   |   |           test_daily_message_limit.cpython-312-pytest-8.3.5.pyc
|   |   |   |           test_email_verification.cpython-312-pytest-8.3.4.pyc
|   |   |   |           test_email_verification.cpython-312-pytest-8.3.5.pyc
|   |   |   |           
|   |   |   +---serializers
|   |   |   |   +---auth
|   |   |   |   |   |   test_register.py
|   |   |   |   |   |   test_session_serializers.py
|   |   |   |   |   |   
|   |   |   |   |   \---__pycache__
|   |   |   |   |           test_register.cpython-312-pytest-8.3.4.pyc
|   |   |   |   |           test_register.cpython-312-pytest-8.3.5.pyc
|   |   |   |   |           test_session_serializers.cpython-312-pytest-8.3.4.pyc
|   |   |   |   |           test_session_serializers.cpython-312-pytest-8.3.5.pyc
|   |   |   |   |           
|   |   |   |   +---password
|   |   |   |   |   |   test_change_password.py
|   |   |   |   |   |   test_reset_password.py
|   |   |   |   |   |   test_reset_password_send_code.py
|   |   |   |   |   |   
|   |   |   |   |   \---__pycache__
|   |   |   |   |           test_change_password.cpython-312-pytest-8.3.4.pyc
|   |   |   |   |           test_change_password.cpython-312-pytest-8.3.5.pyc
|   |   |   |   |           test_reset_password.cpython-312-pytest-8.3.4.pyc
|   |   |   |   |           test_reset_password.cpython-312-pytest-8.3.5.pyc
|   |   |   |   |           test_reset_password_send_code.cpython-312-pytest-8.3.4.pyc
|   |   |   |   |           test_reset_password_send_code.cpython-312-pytest-8.3.5.pyc
|   |   |   |   |           
|   |   |   |   +---user
|   |   |   |   |       test_user_preferences_s.py
|   |   |   |   |       
|   |   |   |   \---verification
|   |   |   |       |   test_send_verification_code.py
|   |   |   |       |   
|   |   |   |       \---__pycache__
|   |   |   |               test_send_verification_code.cpython-312-pytest-8.3.4.pyc
|   |   |   |               test_send_verification_code.cpython-312-pytest-8.3.5.pyc
|   |   |   |               
|   |   |   \---views
|   |   |       +---auth
|   |   |       |   |   test_login.py
|   |   |       |   |   test_logout.py
|   |   |       |   |   test_register_view.py
|   |   |       |   |   
|   |   |       |   \---__pycache__
|   |   |       |           test_login.cpython-312-pytest-8.3.4.pyc
|   |   |       |           test_login.cpython-312-pytest-8.3.5.pyc
|   |   |       |           test_logout.cpython-312-pytest-8.3.4.pyc
|   |   |       |           test_logout.cpython-312-pytest-8.3.5.pyc
|   |   |       |           test_register_view.cpython-312-pytest-8.3.4.pyc
|   |   |       |           test_register_view.cpython-312-pytest-8.3.5.pyc
|   |   |       |           
|   |   |       +---password
|   |   |       |   |   test_change_password_view.py
|   |   |       |   |   test_reset_password_send_code_view.py
|   |   |       |   |   test_reset_password_view.py
|   |   |       |   |   
|   |   |       |   \---__pycache__
|   |   |       |           test_change_password_view.cpython-312-pytest-8.3.4.pyc
|   |   |       |           test_change_password_view.cpython-312-pytest-8.3.5.pyc
|   |   |       |           test_reset_password_send_code_view.cpython-312-pytest-8.3.4.pyc
|   |   |       |           test_reset_password_send_code_view.cpython-312-pytest-8.3.5.pyc
|   |   |       |           test_reset_password_view.cpython-312-pytest-8.3.4.pyc
|   |   |       |           test_reset_password_view.cpython-312-pytest-8.3.5.pyc
|   |   |       |           
|   |   |       \---verification
|   |   |           |   test_send_verification_code_view.py
|   |   |           |   
|   |   |           \---__pycache__
|   |   |                   test_send_verification_code_view.cpython-312-pytest-8.3.4.pyc
|   |   |                   test_send_verification_code_view.cpython-312-pytest-8.3.5.pyc
|   |   |                   
|   |   +---urls
|   |   |   |   auth.py
|   |   |   |   password.py
|   |   |   |   user_preferences.py
|   |   |   |   verfication.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           auth.cpython-312.pyc
|   |   |           password.cpython-312.pyc
|   |   |           user_preferences.cpython-312.pyc
|   |   |           verfication.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---views
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   +---auth
|   |   |   |   |   login.py
|   |   |   |   |   logout.py
|   |   |   |   |   register.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           login.cpython-312.pyc
|   |   |   |           logout.cpython-312.pyc
|   |   |   |           register.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   +---password
|   |   |   |   |   change_password.py
|   |   |   |   |   reset_password.py
|   |   |   |   |   reset_password_send_code.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           change_password.cpython-312.pyc
|   |   |   |           reset_password.cpython-312.pyc
|   |   |   |           reset_password_send_code.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   +---user
|   |   |   |   |   user_preferences.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           user_preferences.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   +---verfication
|   |   |   |   |   send_verification_code.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           send_verification_code.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   \---__pycache__
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   \---__pycache__
|   |           apps.cpython-312.pyc
|   |           tasks.cpython-312.pyc
|   |           __init__.cpython-312.pyc
|   |           
|   +---books
|   |   |   apps.py
|   |   |   urls.py
|   |   |   __init__.py
|   |   |   
|   |   +---admin
|   |   |   |   author.py
|   |   |   |   book.py
|   |   |   |   book_recommendation.py
|   |   |   |   book_review.py
|   |   |   |   book_view.py
|   |   |   |   category.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           admin.cpython-312.pyc
|   |   |           author.cpython-312.pyc
|   |   |           book.cpython-312.pyc
|   |   |           book_recommendation.cpython-312.pyc
|   |   |           book_view.cpython-312.pyc
|   |   |           category.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---migrations
|   |   |   |   0001_initial.py
|   |   |   |   0002_userbookview.py
|   |   |   |   0003_userbookview_author_userbookview_book_genre.py
|   |   |   |   0004_remove_userbookview_author_and_more.py
|   |   |   |   0005_alter_userbookview_unique_together.py
|   |   |   |   0006_alter_userbookview_unique_together.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           0001_initial.cpython-312.pyc
|   |   |           0002_userbookview.cpython-312.pyc
|   |   |           0003_userbookview_author_userbookview_book_genre.cpython-312.pyc
|   |   |           0004_remove_userbookview_author_and_more.cpython-312.pyc
|   |   |           0005_alter_userbookview_unique_together.cpython-312.pyc
|   |   |           0006_alter_userbookview_unique_together.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---models
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   +---catalog
|   |   |   |   |   author.py
|   |   |   |   |   book.py
|   |   |   |   |   category.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           author.cpython-312.pyc
|   |   |   |           book.cpython-312.pyc
|   |   |   |           category.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   +---review
|   |   |   |   |   book_recommendation.py
|   |   |   |   |   book_review.py
|   |   |   |   |   book_view.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           book_recommendation.cpython-312.pyc
|   |   |   |           book_review.cpython-312.pyc
|   |   |   |           book_view.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   \---__pycache__
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---serializers
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   +---catalog
|   |   |   |   |   author.py
|   |   |   |   |   book.py
|   |   |   |   |   category.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           author.cpython-312.pyc
|   |   |   |           book.cpython-312.pyc
|   |   |   |           category.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   +---review
|   |   |   |   |   book_recommendation.py
|   |   |   |   |   book_review.py
|   |   |   |   |   book_view.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           book_recommendation.cpython-312.pyc
|   |   |   |           book_review.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   \---__pycache__
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---signals
|   |   |   |   signals.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           signals.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---tests
|   |   |   +---models
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   +---catalog
|   |   |   |   |   |   test_author.py
|   |   |   |   |   |   test_book.py
|   |   |   |   |   |   test_category.py
|   |   |   |   |   |   __init__.py
|   |   |   |   |   |   
|   |   |   |   |   \---__pycache__
|   |   |   |   |           test_author.cpython-312-pytest-8.3.4.pyc
|   |   |   |   |           test_author.cpython-312-pytest-8.3.5.pyc
|   |   |   |   |           test_book.cpython-312-pytest-8.3.4.pyc
|   |   |   |   |           test_book.cpython-312-pytest-8.3.5.pyc
|   |   |   |   |           test_category.cpython-312-pytest-8.3.4.pyc
|   |   |   |   |           test_category.cpython-312-pytest-8.3.5.pyc
|   |   |   |   |           __init__.cpython-312.pyc
|   |   |   |   |           
|   |   |   |   +---review
|   |   |   |   |   |   test_book_review.py
|   |   |   |   |   |   
|   |   |   |   |   \---__pycache__
|   |   |   |   |           test_book_review.cpython-312-pytest-8.3.4.pyc
|   |   |   |   |           test_book_review.cpython-312-pytest-8.3.5.pyc
|   |   |   |   |           
|   |   |   |   \---__pycache__
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   +---serializers
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   +---catalog
|   |   |   |   |   |   test_author.py
|   |   |   |   |   |   test_book_serializers.py
|   |   |   |   |   |   test_category.py
|   |   |   |   |   |   
|   |   |   |   |   \---__pycache__
|   |   |   |   |           test_author.cpython-312-pytest-8.3.4.pyc
|   |   |   |   |           test_author.cpython-312-pytest-8.3.5.pyc
|   |   |   |   |           test_book_serializers.cpython-312-pytest-8.3.4.pyc
|   |   |   |   |           test_book_serializers.cpython-312-pytest-8.3.5.pyc
|   |   |   |   |           test_category.cpython-312-pytest-8.3.4.pyc
|   |   |   |   |           test_category.cpython-312-pytest-8.3.5.pyc
|   |   |   |   |           
|   |   |   |   +---review
|   |   |   |   |   |   test_book_review_serializer.py
|   |   |   |   |   |   
|   |   |   |   |   \---__pycache__
|   |   |   |   |           test_book_review_serializer.cpython-312-pytest-8.3.4.pyc
|   |   |   |   |           test_book_review_serializer.cpython-312-pytest-8.3.5.pyc
|   |   |   |   |           
|   |   |   |   \---__pycache__
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   \---views
|   |   |       |   __init__.py
|   |   |       |   
|   |   |       +---catalog
|   |   |       |   |   test_author.py
|   |   |       |   |   test_book_view.py
|   |   |       |   |   test_category.py
|   |   |       |   |   __init__.py
|   |   |       |   |   
|   |   |       |   \---__pycache__
|   |   |       |           test_author.cpython-312-pytest-8.3.4.pyc
|   |   |       |           test_author.cpython-312-pytest-8.3.5.pyc
|   |   |       |           test_book_view.cpython-312-pytest-8.3.4.pyc
|   |   |       |           test_book_view.cpython-312-pytest-8.3.5.pyc
|   |   |       |           test_category.cpython-312-pytest-8.3.4.pyc
|   |   |       |           test_category.cpython-312-pytest-8.3.5.pyc
|   |   |       |           __init__.cpython-312.pyc
|   |   |       |           
|   |   |       +---review
|   |   |       |   |   test_book_review_view.py
|   |   |       |   |   
|   |   |       |   \---__pycache__
|   |   |       |           test_book_review_view.cpython-312-pytest-8.3.4.pyc
|   |   |       |           test_book_review_view.cpython-312-pytest-8.3.5.pyc
|   |   |       |           
|   |   |       \---__pycache__
|   |   |               __init__.cpython-312.pyc
|   |   |               
|   |   +---urls
|   |   |   |   author.py
|   |   |   |   book.py
|   |   |   |   book_recommendation.py
|   |   |   |   book_review.py
|   |   |   |   category.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           author.cpython-312.pyc
|   |   |           book.cpython-312.pyc
|   |   |           book_recommendation.cpython-312.pyc
|   |   |           book_review.cpython-312.pyc
|   |   |           category.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---views
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   +---catalog
|   |   |   |   |   author.py
|   |   |   |   |   book.py
|   |   |   |   |   category.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           author.cpython-312.pyc
|   |   |   |           book.cpython-312.pyc
|   |   |   |           category.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   +---review
|   |   |   |   |   book_recommendation.py
|   |   |   |   |   book_review.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           book_recommendation.cpython-312.pyc
|   |   |   |           book_review.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   \---__pycache__
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   \---__pycache__
|   |           apps.cpython-312.pyc
|   |           __init__.cpython-312.pyc
|   |           
|   +---event_manager
|   |   |   apps.py
|   |   |   urls.py
|   |   |   __init__.py
|   |   |   
|   |   +---admin
|   |   |   |   event_schedule.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           event_schedule.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---migrations
|   |   |   |   0001_initial.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           0001_initial.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---models
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   +---event
|   |   |   |   |   event_schedule.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           event_schedule.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   \---__pycache__
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---serializers
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   +---event
|   |   |   |   |   event_schedule.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           event_schedule.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   \---__pycache__
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---tests
|   |   |   +---models
|   |   |   |   |   test_event_schedule.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           test_event_schedule.cpython-312-pytest-8.3.5.pyc
|   |   |   |           
|   |   |   +---serializers
|   |   |   |   |   test_event_schedule_s.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           test_event_schedule_s.cpython-312-pytest-8.3.5.pyc
|   |   |   |           
|   |   |   \---views
|   |   |       |   test_event_schedule_v.py
|   |   |       |   
|   |   |       \---__pycache__
|   |   |               test_event_schedule_v.cpython-312-pytest-8.3.5.pyc
|   |   |               
|   |   +---urls
|   |   |   |   event_schedule.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           event_schedule.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---views
|   |   |   |   event_schedule.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           event_schedule.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   \---__pycache__
|   |           apps.cpython-312.pyc
|   |           __init__.cpython-312.pyc
|   |           
|   +---library
|   |   |   asgi.py
|   |   |   celery.py
|   |   |   pytest.ini
|   |   |   settings.py
|   |   |   urls.py
|   |   |   wsgi.py
|   |   |   __init__.py
|   |   |   
|   |   +---.pytest_cache
|   |   |   |   .gitignore
|   |   |   |   CACHEDIR.TAG
|   |   |   |   README.md
|   |   |   |   
|   |   |   \---v
|   |   |       \---cache
|   |   |               nodeids
|   |   |               stepwise
|   |   |               
|   |   \---__pycache__
|   |           celery.cpython-312.pyc
|   |           settings.cpython-312.pyc
|   |           urls.cpython-312.pyc
|   |           wsgi.cpython-312.pyc
|   |           __init__.cpython-312.pyc
|   |           
|   +---media
|   |   +---authors
|   |   |   \---2025
|   |   |       \---03
|   |   |           \---26
|   |   |                   6b031465-d302-4961-94ce-e92a789f39df.jpg
|   |   |                   
|   |   +---book_images
|   |   |   \---2025
|   |   |       \---03
|   |   |           \---26
|   |   |                   Flux_Dev_1__1879cu_il_Kiik_Albertin_glii_Video_19cu_sr_aid_khn_1.jpeg
|   |   |                   Flux_Dev_A_5yearold_child_in_a_moment_of_wonder_holding_a_comp_0.jpeg
|   |   |                   
|   |   +---ebooks
|   |   |       Learn_Python_3_the_Hard_Way_A_Very_Simple_Introduction_to_the_Terrifyingly.pdf
|   |   |       
|   |   +---event_images
|   |   |       43ccb52c03c85c71e64c12b4f2f67cb7.jpg
|   |   |       43ccb52c03c85c71e64c12b4f2f67cb7_ESS5IA8.jpg
|   |   |       download.jfif
|   |   |       download_3rXtCtY.jfif
|   |   |       download_uR9mCfv.jfif
|   |   |       Flux_Dev_updatedpromptA_vibrant_and_dynamic_illustration_depic_0.jpeg
|   |   |       
|   |   \---event_videos
|   |           Albert_Einstein__Bir_Dahinin_Yolculugu2_ci_kisim.mp4
|   |           Albert_Einstein__Bir_Dahinin_Yolculugu2_ci_kisim_tgQdOuH.mp4
|   |           Albert_Einstein__Bir_Dahinin_Yolculugu_1-ci_bölüm.mp4
|   |           Albert_Einstein__Bir_Dahinin_Yolculugu_1-ci_bölüm_peEipZy.mp4
|   |           
|   +---notifications
|   |   |   apps.py
|   |   |   tasks.py
|   |   |   tests.py
|   |   |   urls.py
|   |   |   views.py
|   |   |   __init__.py
|   |   |   
|   |   +---admin
|   |   |   |   overdue_notification.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           overdue_notification.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---migrations
|   |   |   |   0001_initial.py
|   |   |   |   0002_remove_overduenotification_next_reminder_date.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           0001_initial.cpython-312.pyc
|   |   |           0002_remove_overduenotification_next_reminder_date.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---models
|   |   |   |   overdue_notification.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           overdue_notification.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---serializers
|   |   |       overdue_notification.py
|   |   |       __init__.py
|   |   |       
|   |   +---signals
|   |   |       signals.py
|   |   |       __init__.py
|   |   |       
|   |   \---__pycache__
|   |           apps.cpython-312.pyc
|   |           tasks.cpython-312.pyc
|   |           __init__.cpython-312.pyc
|   |           
|   +---payments
|   |   |   apps.py
|   |   |   urls.py
|   |   |   __init__.py
|   |   |   
|   |   +---admin
|   |   |   |   payment.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           payment.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---migrations
|   |   |   |   0001_initial.py
|   |   |   |   0002_alter_payment_amount_alter_payment_book_and_more.py
|   |   |   |   0003_payment_is_refunded_payment_metadata_and_more.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           0001_initial.cpython-312.pyc
|   |   |           0002_alter_payment_amount_alter_payment_book_and_more.cpython-312.pyc
|   |   |           0003_payment_is_refunded_payment_metadata_and_more.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---models
|   |   |   |   payment.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           payment.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---serializers
|   |   |   |   payment_serializers.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           payment_serializers.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---urls
|   |   |   |   payment_url.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           payment_url.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---views
|   |   |   |   payment_view.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           payment_view.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   \---__pycache__
|   |           apps.cpython-312.pyc
|   |           __init__.cpython-312.pyc
|   |           
|   +---services
|   |   |   __init__.py
|   |   |   
|   |   +---auth
|   |   |   |   email_service.py
|   |   |   |   user_services.py
|   |   |   |   verification_service.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           email_service.cpython-312.pyc
|   |   |           user_services.cpython-312.pyc
|   |   |           verification_service.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   \---__pycache__
|   |           rental.cpython-312.pyc
|   |           __init__.cpython-312.pyc
|   |           
|   +---transactions
|   |   |   apps.py
|   |   |   tasks.py
|   |   |   urls.py
|   |   |   __init__.py
|   |   |   
|   |   +---admin
|   |   |   |   overdue_fine.py
|   |   |   |   purchase_history.py
|   |   |   |   rental_history.py
|   |   |   |   rental_price.py
|   |   |   |   rental_schedule.py
|   |   |   |   sale_price.py
|   |   |   |   sale_transaction.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           overdue_fine.cpython-312.pyc
|   |   |           purchase_history.cpython-312.pyc
|   |   |           rental_history.cpython-312.pyc
|   |   |           rental_price.cpython-312.pyc
|   |   |           rental_schedule.cpython-312.pyc
|   |   |           sale_price.cpython-312.pyc
|   |   |           sale_transaction.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---migrations
|   |   |   |   0001_initial.py
|   |   |   |   0002_alter_rentalschedule_rental_end_date.py
|   |   |   |   0003_alter_rentalschedule_rental_end_date.py
|   |   |   |   0004_alter_overduefine_fine_amount.py
|   |   |   |   0005_alter_overduefine_fine_amount.py
|   |   |   |   0006_alter_purchasehistory_book_and_more.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           0001_initial.cpython-312.pyc
|   |   |           0002_alter_rentalschedule_rental_end_date.cpython-312.pyc
|   |   |           0002_alter_saleprice_book.cpython-312.pyc
|   |   |           0002_alter_saleprice_unique_together.cpython-312.pyc
|   |   |           0002_saleprice_created_at.cpython-312.pyc
|   |   |           0003_alter_rentalschedule_rental_end_date.cpython-312.pyc
|   |   |           0003_alter_saleprice_unique_together.cpython-312.pyc
|   |   |           0004_alter_overduefine_fine_amount.cpython-312.pyc
|   |   |           0004_remove_rentalprice_price_rentalprice_price_1_month_and_more.cpython-312.pyc
|   |   |           0005_alter_overduefine_fine_amount.cpython-312.pyc
|   |   |           0006_alter_purchasehistory_book_and_more.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---models
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   +---history
|   |   |   |   |   purchase_history.py
|   |   |   |   |   rental_history.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           purchase_history.cpython-312.pyc
|   |   |   |           rental_history.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   +---rental
|   |   |   |   |   overdue_fine.py
|   |   |   |   |   rental_price.py
|   |   |   |   |   rental_schedule.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           overdue_fine.cpython-312.pyc
|   |   |   |           rental_price.cpython-312.pyc
|   |   |   |           rental_schedule.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   +---sale
|   |   |   |   |   sale_price.py
|   |   |   |   |   sale_transaction.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           sale_price.cpython-312.pyc
|   |   |   |           sale_transaction.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   \---__pycache__
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---serializers
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   +---history
|   |   |   |   |   purchase_history.py
|   |   |   |   |   rental_history.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           purchase_history.cpython-312.pyc
|   |   |   |           rental_history.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   +---rental
|   |   |   |   |   overdue_fine.py
|   |   |   |   |   rental_price.py
|   |   |   |   |   rental_schedule.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           overdue_fine.cpython-312.pyc
|   |   |   |           rental_price.cpython-312.pyc
|   |   |   |           rental_schedule.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   +---sale
|   |   |   |   |   sale_price.py
|   |   |   |   |   sale_transaction.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           sale_price.cpython-312.pyc
|   |   |   |           sale_transaction.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   \---__pycache__
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---signals
|   |   |   |   signals.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           signals.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---urls
|   |   |   |   overdue_fine_url.py
|   |   |   |   purchase_history_url.py
|   |   |   |   rental_history_url.py
|   |   |   |   rental_price_url.py
|   |   |   |   rental_schedule_url.py
|   |   |   |   sale_price_url.py
|   |   |   |   sale_transaction_url.py
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   \---__pycache__
|   |   |           overdue_fine_url.cpython-312.pyc
|   |   |           purchase_history_url.cpython-312.pyc
|   |   |           rental_history_url.cpython-312.pyc
|   |   |           rental_price_url.cpython-312.pyc
|   |   |           rental_schedule_url.cpython-312.pyc
|   |   |           sale_price_url.cpython-312.pyc
|   |   |           sale_transaction_url.cpython-312.pyc
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   +---views
|   |   |   |   __init__.py
|   |   |   |   
|   |   |   +---history
|   |   |   |   |   purchase_history.py
|   |   |   |   |   rental_history.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           purchase_history.cpython-312.pyc
|   |   |   |           rental_history.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   +---rental
|   |   |   |   |   overdue_fine.py
|   |   |   |   |   rental_price.py
|   |   |   |   |   rental_schedule.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           overdue_fine.cpython-312.pyc
|   |   |   |           rental_price.cpython-312.pyc
|   |   |   |           rental_schedule.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   +---sale
|   |   |   |   |   sale_price.py
|   |   |   |   |   sale_transaction.py
|   |   |   |   |   __init__.py
|   |   |   |   |   
|   |   |   |   \---__pycache__
|   |   |   |           sale_price.cpython-312.pyc
|   |   |   |           sale_transaction.cpython-312.pyc
|   |   |   |           __init__.cpython-312.pyc
|   |   |   |           
|   |   |   \---__pycache__
|   |   |           __init__.cpython-312.pyc
|   |   |           
|   |   \---__pycache__
|   |           admin.cpython-312.pyc
|   |           apps.cpython-312.pyc
|   |           tasks.cpython-312.pyc
|   |           __init__.cpython-312.pyc
|   |           
|   \---utils
|       |   __init__.py
|       |   
|       +---constats
|       |   |   time_intervals.py
|       |   |   __init__.py
|       |   |   
|       |   \---__pycache__
|       |           time_intervals.cpython-312.pyc
|       |           __init__.cpython-312.pyc
|       |           
|       +---slug
|       |   |   slug.py
|       |   |   slug_manager.py
|       |   |   __init__.py
|       |   |   
|       |   \---__pycache__
|       |           slug.cpython-312.pyc
|       |           slug_manager.cpython-312.pyc
|       |           __init__.cpython-312.pyc
|       |           
|       +---verification_code
|       |   |   verification_code.py
|       |   |   __init__.py
|       |   |   
|       |   \---__pycache__
|       |           verification_code.cpython-312.pyc
|       |           __init__.cpython-312.pyc
|       |           
|       \---__pycache__
|               __init__.cpython-312.pyc
|               
\---scripts
        createsuperuser.sh
        makemigrations_docker.sh
        migrate_docker.sh
        run_celery.sh
        start_docker.sh
        stop_docker.sh
        
