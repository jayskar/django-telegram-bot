from django.urls import Resolver404

class HandlerNotFound(Exception):
    pass


class HandlerResolver(object):


    def resolve(self, update):
        try:
            resolver_match = self.resolver.resolve(update.message.text)
            return resolver_match
        except Resolver404:
            raise HandlerNotFound("No handler configured for  %s" % update.message.text)
