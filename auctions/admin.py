from django.contrib import admin

from .models import User , comment , bids , listing , category ,  watchlist 
# Register your models here.
admin.site.register(User)
admin.site.register(comment)
admin.site.register(bids)
admin.site.register(listing)
admin.site.register(category)
admin.site.register(watchlist)

# Register your models here.
