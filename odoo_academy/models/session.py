# -*- coding: utf-8 -*-
import string
from odoo import models, fields, api


class Course(models.Model):
    _name = 'academy.session'
    _description = 'Session Info'

    # if it's Many2one, add '_id' after the field name
    course_id = fields.Many2one(
        comodel_name='academy.course', string='Course', ondelete='cascade', required=True)
    name = fields.Char(string='Title', related='course_id.name')
    instructor_id = fields.Many2one(
        comodel_name='res.partner', string='Instructor')
    # if it's Many2many, add '_ids' after the field name
    student_ids = fields.Many2many(
        comodel_name='res.users', string='Add more students~~')
