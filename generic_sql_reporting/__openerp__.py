# -*- coding: utf-8 -*-
##############################################################################
#
#    printers_kazacube module for OpenERP, Specific changes for Kazacube
#    Copyright (C) 2013 SYLEAM Info Services (<http://www.Syleam.fr/>)
#              Sylvain Garancher <sylvain.garancher@syleam.fr>
#
#    This file is a part of printers_kazacube
#
#    printers_kazacube is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    printers_kazacube is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'GENERIC SQL REPORTING',
    'version': '1.0',
    'category': 'Custom',
    'description': """Ce module est conçu pour générer des rapports sql """,
    'author': 'STAROIL MALI',
    'website': '',
    'depends': ["base"],
    'update_xml': ['sql_request_view.xml',
                   'sql_report_wizard_view.xml'],
    'test': [],
    'installable': True,
    'active': True,
    'application':True,
    'license': 'AGPL-3',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
