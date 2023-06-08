{
    'name': 'NXC Lead Qualification Addon',
    'version': '15.0',
    'category': 'contacts',
    'summary': 'Adds strategic account plan notebook page. This page includes market qualification and lead qualification subsections. Outputs MQL score for prioritizing leads.',
    'description': 'This custom module was developed for Next Chapter Manufacturing to enrich lead tracking efforts in the contacts module.',
    'author': 'Hayden McCarthy',
    'website': 'https://www.nxcmfg.com',
    'license': 'AGPL-3',
    'depends': ['contacts', 'crm'],
    'data': [
        'views/view_nxc_lead_qualification_partner_form.xml',
        'views/view_nxc_lead_qualification_lead_form.xml',
        'views/view_nxc_lead_qualification_lead_kanban.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'static/assets/priority_blue.css',
        ]
    },
    'installable': True,
    'auto_install': False,
}

