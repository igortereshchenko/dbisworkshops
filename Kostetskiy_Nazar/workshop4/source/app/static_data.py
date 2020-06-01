from datetime import datetime

POST1 = {'id': 1, 'body': 'Static post for demonstration. Not in db.\n'
                          'Mauris volutpat ante eget odio pharetra, facilisis semper justo ultricies.'
                          ' Ut euismod massa sit amet nunc malesuada imperdiet. Integer auctor lacus odio,'
                          ' lobortis aliquet massa tincidunt quis.'
                          ' Praesent sollicitudin tellus dolor, molestie fermentum elit sodales sit amet.'
                          ' Aenean ac neque nec quam ultricies vulputate.'
                          ' Nam mattis nulla id nibh ultrices, scelerisque fringilla nisl fermentum.'
                          ' Nunc varius aliquam nunc vitae sodales. ',
         'position': 'Senior Software Engineer',
         'created_at': datetime.strftime(datetime.now(), "%Y.%m.%d "), 'price_usd': 2500,
         'user_id': 1050, 'comments': []}
POST2 = {'id': 2, 'body': 'Static post for demonstration. Not in db.\n'
                          'Nam sed sem id ipsum luctus mollis.'
                          ' Fusce vehicula, purus in eleifend eleifend,'
                          ' lacus ipsum auctor erat, non commodo magna justo in lectus.'
                          ' Aenean felis enim, iaculis non dolor quis, gravida consequat erat.'
                          ' Vestibulum et faucibus diam, vel luctus nisl.'
                          ' Vivamus elit ante, posuere eu finibus quis, porta et est.'
                          ' Nulla gravida vulputate viverra.'
                          ' Maecenas quis neque ut diam congue tempor. '
                          ' Ut diam congue tempor. ',
         'position': 'Junior Test Engineer',
         'created_at': datetime.strftime(datetime.now(), "%Y.%m.%d "), 'price_usd': 400,
         'user_id': 1515, 'comments': []}

ALL_STATIC_POSTS = [POST1, POST2]