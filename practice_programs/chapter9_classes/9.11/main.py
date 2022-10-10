from admin import*

admin_rights = Admin('Sadaf','Hina', 'abc@gmail.com','Karachi')
admin_rights.describe_user()
admin_rights.privileges.privileges = ['can change password','can hide files','can add/delete user']
admin_rights.privileges.show_privileges()