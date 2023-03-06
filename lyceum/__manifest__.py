{
    'name': 'lyceum',
    'application': True,
    'license': 'LGPL-3',
    'installable': True,
    'depends':['base','mail'],
    "data": [
        'security/ir.model.access.csv',
        'views/lyceum_tags_view.xml',
        'views/lyceum_create_view.xml',
        'views/event_create_view.xml',
        'views/lyceum_menus.xml',
        'report/event_create_report.xml',
        'report/event_create_templates.xml',
        # 'views/intern_allocation.xml',
        # # 'views/action_intern_allocation.xml',
        # 'views/intern_role_allocation.xml',
        # 'views/desk_allocation_view.xml',
        # 'views/laptop_allocation_view.xml',
        # 'views/view_equipment.xml',
        # 'views/college_information_view.xml',
        # 'views/document_upload_view.xml',
        # 'views/res_users_view.xml',
    ],
    'demo' : 
    [
        'demo/demo_data.xml'
    ]
}
