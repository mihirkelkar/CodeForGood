import json

class MockResponses():

  ##GET /user/ID
  #Mockups used to test responses on test pages
  def user_profile(request, user_id):
    user = {
      'id': user_id,
      'profile_image': {
        'thumb': 'http://ionicframework.com/img/docs/spengler.jpg',
        'full_size': 'http://www.wired.com/images_blogs/threatlevel/2012/03/copyright-troll.jpg'
      },
      'name': {
        'first': 'Student',
        'last': 'Mentee'
      },
      'role': 'mentee',
      'email': 'mentee@email.com',
      'school': 'Harker High School',
      'grade': '12th',
      'age': '18',
      'mentor_id': '12'
    }

    return json.dumps(user)

  ###GET /user/ID/messages/
  #Mock up used to test whether message threads are getting propely displayed.
  def user_messages(request, user_id):
    messages =   [{'sender_name':'Adult Mentor',
                 'timestamp': 'Friday, 3:05 PM',
                 'message_content': 'Hey, I just met you...',
                 'attachment': '',
                 'user_thumb':'http://ionicframework.com/img/docs/spengler.jpg',
                 'id': '1'},
                 {'sender_name':'Adult Mentor',
                 'timestamp': 'Friday, 3:05 PM',
                 'message_content': '...and this is crazy...',
                 'attachment': '',
                 'user_thumb':'http://ionicframework.com/img/docs/spengler.jpg',
                 'id': '2'},
                 {'sender_name':'Friday, 3:05 PM',
                 'timestamp': '0000:MM:DD:YYYY',
                 'message_content': '...but I AM a college graduate...',
                 'attachment': '',
                 'user_thumb':'http://ionicframework.com/img/docs/spengler.jpg',
                 'id': '3'},
                 {'sender_name':'Adult Mentor',
                 'timestamp': 'Friday, 3:06 PM',
                 'message_content': '...so be my mentee?',
                 'attachment': '',
                 'user_thumb':'http://ionicframework.com/img/docs/spengler.jpg',
                 'id': '4'},
                 {'sender_name':'Student Mentee',
                 'timestamp': 'Friday, 3:07 PM',
                 'message_content': 'Lol K',
                 'attachment': '',
                 'user_thumb':'http://ionicframework.com/img/docs/stantz.jpg',
                 'id': '5'},
                 ]

    return json.dumps(messages)

  ###POST /user/ID/messages/message_id/
    return 'SUCCESS!'
  #Mocking all pairs that exist under the supervision of a given PC.
  def pc_pairs(request):
    pairs = [{'mentor': {'id': '1',
                         'profile_image': {'thumb': '',
                                           'full_size': ''},
                          'name': {'first': 'Adult',
                                   'last': 'Mentor'}
                        },
              'mentee': {'id': '2',
                         'profile_image': {'thumb': '',
                                           'full_size': ''},
                          'name': {'first': 'Student',
                                   'last': 'Mentee'}
                        }
              },
              {'mentor': {'id': '3',
                         'profile_image': {'thumb': '',
                                           'full_size': ''},
                          'name': {'first': 'Adult',
                                   'last': 'Mentor'}
                        },
              'mentee': {'id': '4',
                         'profile_image': {'thumb': '',
                                           'full_size': ''},
                          'name': {'first': 'Student',
                                   'last': 'Mentee'}
                        }
              },
              {'mentor': {'id': '5',
                         'profile_image': {'thumb': '',
                                           'full_size': ''},
                          'name': {'first': 'Adult',
                                   'last': 'Mentor'}
                        },
              'mentee': {'id': '6',
                         'profile_image': {'thumb': '',
                                           'full_size': ''},
                          'name': {'first': 'Student',
                                   'last': 'Mentee'}
                        }
              },
              {'mentor': {'id': '7',
                         'profile_image': {'thumb': '',
                                           'full_size': ''},
                          'name': {'first': 'Adult',
                                   'last': 'Mentor'}
                        },
              'mentee': {'id': '8',
                         'profile_image': {'thumb': '',
                                           'full_size': ''},
                          'name': {'first': 'Student',
                                   'last': 'Mentee'}
                        }
              },
              {'mentor': {'id': '9',
                         'profile_image': {'thumb': '',
                                           'full_size': ''},
                          'name': {'first': 'Adult',
                                   'last': 'Mentor'}
                        },
              'mentee': {'id': '10',
                         'profile_image': {'thumb': '',
                                           'full_size': ''},
                          'name': {'first': 'Student',
                                   'last': 'Mentee'}
                        }
              }]

    return json.dumps(pairs)

  def success(request):
    message = {'status': 'SUCCESS!'}

    return json.dumps(message)

  def failure(request):
    message = {'status': 'FAILED!'}

    return json.dumps(message)

  def error(request):
    message = {'status': 'ERROR!'}

    return json.dumps(message)

  def message_details(request, user_id, message_id):
    message = {'sender_name':'Adult Mentor',
               'recipient_name':'Student Mentee',
               'timestamp': 'Sent Saturday, 10:05AM',
               'message_content': 'Quisque scelerisque ut velit et euismod. Praesent quis cursus est. Nulla ut nibh ut quam malesuada finibus sit amet non magna. Vivamus massa arcu, luctus quis porta id, elementum vel enim. Integer finibus leo eros, in lobortis metus lobortis non. Curabitur sollicitudin ex eget risus fermentum elementum malesuada vitae lorem. Nunc egestas diam non interdum dignissim. Suspendisse maximus luctus lorem, in accumsan lorem viverra sit amet. ',
               'attachment': '',
               'user_thumb':'',
               'id': '1'}

    return json.dumps(message)
