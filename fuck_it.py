import requests
from data.leecode import *

heades = {
    'dnt': '1',
    'accept-language': 'en-US,en;q=0.9,uk;q=0.8,ru;q=0.7,fr;q=0.6,zh-TW;q=0.5,zh;q=0.4,nl;q=0.3',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'content-type': 'application/json, text/plain',
    'accept': '*/*',
    'referer': 'https://leetcode.com/problems/merge-k-sorted-lists/description/',
    'authority': 'leetcode.com',
    'cookie': '__cfduid=dd5e143c656c7e7144c90c519879ff02f1522707971; csrftoken=jgBpcECmDpgRR84FRwIv1bvyZgVKnzyHCqtSg0dLnxmb3AE2QTAi5igErpssnPvM; LEETCODE_SESSION=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Im1zb2Vkb3YiLCJ1c2VyX3NsdWciOiJtc29lZG92IiwiX2F1dGhfdXNlcl9pZCI6IjIxODk0MyIsIlJFTU9URV9BRERSIjoiMjYwMToxOTI6NGM3ZjpmMzFhOjdjNzE6ZGM1MTo0NThjOmNjMjMiLCJ0aW1lc3RhbXAiOiIyMDE4LTA0LTAyIDIyOjI2OjI4LjUxMzU3NCswMDowMCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImFsbGF1dGguYWNjb3VudC5hdXRoX2JhY2tlbmRzLkF1dGhlbnRpY2F0aW9uQmFja2VuZCIsImVtYWlsIjoibXNvZWRvdkBnbWFpbC5jb20iLCJhdmF0YXIiOiJodHRwczovL3MzLWxjLXVwbG9hZC5zMy5hbWF6b25hd3MuY29tL3VzZXJzL21zb2Vkb3YvYXZhdGFyXzE1MjIzNTk4OTgucG5nIiwiX2F1dGhfdXNlcl9oYXNoIjoiZGUyYjhjODAzOWMxMmM2Y2VlYTQxZjgxODc1MTMxODg2ZmFkMTM0ZiIsImlkIjoyMTg5NDMsIklERU5USVRZIjoiMGFjMDY1YzBjZDgwNmYxZTM0MzcwZGFjYWQ5NTBkZTcifQ.NyF_7gRMbW8VHmnupNg3Cmyx-iOsweLziOs19FlDG9w',
    'x-csrftoken': 'jgBpcECmDpgRR84FRwIv1bvyZgVKnzyHCqtSg0dLnxmb3AE2QTAi5igErpssnPvM',
}


def main():
    q = open('introspection.js', 'r').read()
    r = requests.get('https://leetcode.com/graphql',
                     params={'query': q}, headers=heades)

    print(r.content)
    open('leecode_schema.json', 'w').write(r.content.decode('utf-8'))


# if __name__ == '__main__':
#     main()


def query(opt):
    for c in ['facebook', 'amazon', 'google', 'twitter', 'yelp', 'apple', 'microsoft', 'bloomberg']:
        r = requests.get('https://leetcode.com/graphql',
                         params={'query': opt, "operationName": "getCompanyTag", "variables": '{"slug":"%s"}' % c}, headers=heades)

        # print(r.content.decode('utf-8'))
        open(f'question_{c}.json', 'w').write(r.content.decode('utf-8'))
    return r


q = """query getCompanyTag($slug: String!) {
  companyTag(slug: $slug) {
    name
    translatedName
    questions {
      status
      content
      article
      questionId
      questionFrontendId
      title
      titleSlug
      translatedTitle
      stats
      topicTags {
        name
        translatedName
        slug
        __typename
      }
      companyTags {
        name
        translatedName
        slug
        __typename
      }
      __typename
    }
    __typename
  }
}
"""

# print(Query.get())
# print(q)
# query(q)
