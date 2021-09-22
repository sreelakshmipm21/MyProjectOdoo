{
    'name': 'Event Management',
    'version': '1.0',
    'sequence': '-100',
    'category': 'Productivity',
    'description': """Event Management""",
    'depends': ['mail'],
    'data': [
             'security/ir.model.access.csv',
             'views/booking.xml',
             'views/eventtype.xml',
             'views/services.xml',
             'views/catering.xml',
             'views/catering_menu.xml',
             'demo/event_type_demo.xml',
             'demo/service_demo.xml'],
    'demo': [],
    'test': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}