

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The code in this program will ask a user for their facebook email, password, a valid graph API query,
# a valid graph API access_token, and a file name(preferably a Python file) to store the JSON response into
# Upon the programs data gathering completion, the data can be accessed from Python by importing "structure"
# from the name of the file chosen by the user
import mechanize
import cookielib
import os
import json

raw_api = 'https://graph.facebook.com/{0}?fields={1}&access_token={2}'
def make_data_structure(email, password, query, access_token, filename):
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_cookiejar(cj)
        br.addheaders = [('User-Agent', 'Mozilla/5.0(X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        br.set_debug_http(True)
        br.set_debug_redirects(True)
        br.set_debug_responses(True)
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.set_handle_equiv(True)
        br.set_handle_gzip(True)
        br.open('http://www.facebook.com')
        br.select_form(nr=0)
        br.set_all_readonly(False)
        br.form['email'] = email
        br.form['pass'] = password
        br.submit()
        the_structure = {}
        the_structure['data'] = []
        # use the graph API to return your id
        br.open(raw_api.format('me', 'id', access_token))
        my_id = json.loads(br.response().read())['id']
        # create a data object of your friends
        br.open(raw_api.format(my_id, 'friends', access_token))
        friends_response = json.loads(br.response().read())     
        # iterate through all of your friends and make a graph API call for each of them with the
        # specified query parameters
        for friend in friends_response['friends']['data']:
                our_friends_id = friend['id']
                the_api_string = raw_api.format(our_friends_id, query, access_token)
                br.open(the_api_string)
                json_response_from_facebook = br.response().read()
                json_handled_response = json.loads(json_response_from_facebook)
                the_structure['data'].append(json_handled_response)
        f = open(filename, "w")
        stringified_structure = json.dumps(the_structure)
        f.write("structure = %s" % stringified_structure)

def main():
        print '\n\nYou will need a valid access_token generated from https://developers.facebook.com/tools/explorer\n\n'
        email = raw_input('Enter your facebook email: ')
        password = raw_input('Enter your facebook password: ')
        query = raw_input('Enter query for spot 1 of %s: ' % raw_api)
        access_token = raw_input('Enter access token: ')
        filename = raw_input('Enter a filename to put the data into: ')
        make_data_structure(email, password, query, access_token, filename)
        print "A facebook json object containing data from the FACEBOOK API with a query of {0} on all of your friends.\nThe document can be found in the {1} file".format(query, filename)

if __name__ == '__main__':
        main()
