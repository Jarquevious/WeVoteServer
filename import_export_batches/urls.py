# import_export_batches/urls.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.conf.urls import re_path

from . import views_admin


urlpatterns = [
    re_path(r'^$', views_admin.batches_home_view, name='batches_home',),
    re_path(r'^batch_action_list/$', views_admin.batch_action_list_view, name='batch_action_list'),
    re_path(r'^batch_action_list_analyze_process/$', views_admin.batch_action_list_analyze_process_view,
        name='batch_action_list_analyze_process'),
    re_path(r'^batch_action_list_assign_election_to_rows_process/$',
        views_admin.batch_action_list_assign_election_to_rows_process_view,
        name='batch_action_list_assign_election_to_rows_process'),
    re_path(r'^batch_action_list_update_or_create_process/$',
        views_admin.batch_action_list_update_or_create_process_view,
        name='batch_action_list_update_or_create_process'),
    # re_path(r'^batch_action_list_import_update_or_create_rows/$',
    #     views_admin.batch_action_list_import_update_or_create_rows,
    #     name='batch_action_list_import_update_or_create_rows'),
    re_path(r'^batch_header_mapping/$', views_admin.batch_header_mapping_view, name='batch_header_mapping'),
    re_path(r'^batch_header_mapping_process/$',
        views_admin.batch_header_mapping_process_view, name='batch_header_mapping_process'),
    re_path(r'^batch_list/$', views_admin.batch_list_view, name='batch_list'),
    re_path(r'^batch_list_process/$', views_admin.batch_list_process_view, name='batch_list_process'),
    re_path(r'^batch_set_list/$', views_admin.batch_set_list_view, name='batch_set_list'),
    re_path(r'^batch_set_list_process/$', views_admin.batch_set_list_process_view, name='batch_set_list_process'),
    re_path(r'^batch_set_batch_list/$', views_admin.batch_set_batch_list_view, name='batch_set_batch_list'),
    re_path(r'^batch_action_list_export/$', views_admin.batch_action_list_export_view, name='batch_action_list_export'),
    re_path(r'^batch_action_list_export_voters/$',
        views_admin.batch_action_list_export_voters_view, name='batch_action_list_export_voters'),
    re_path(r'^batch_row_action_list_export/$',
        views_admin.batch_row_action_list_export_view, name='batch_row_action_list_export'),
    re_path(r'^batch_process_list/$', views_admin.batch_process_list_view, name='batch_process_list',),
    re_path(r'^batch_process_log_entry_list/$',
        views_admin.batch_process_log_entry_list_view, name='batch_process_log_entry_list',),
    # DEPRECATE batch_process_next_steps
    re_path(r'^batch_process_next_steps/$',
        views_admin.batch_process_next_steps_view, name='batch_process_next_steps'),
    re_path(r'^batch_process_pause_toggle/$',
        views_admin.batch_process_pause_toggle_view, name='batch_process_pause_toggle', ),
    re_path(r'^batch_process_system_toggle/$',
        views_admin.batch_process_system_toggle_view, name='batch_process_system_toggle', ),
    re_path(r'^import_ballot_items_for_location/$',
        views_admin.import_ballot_items_for_location_view, name='import_ballot_items_for_location'),
    re_path(r'^process_next_activity_notices/$',
        views_admin.process_next_activity_notices_view, name='process_next_activity_notices'),
    re_path(r'^process_next_ballot_items/$',
        views_admin.process_next_ballot_items_view, name='process_next_ballot_items'),
    re_path(r'^process_next_general_maintenance/$',
        views_admin.process_next_general_maintenance_view, name='process_next_general_maintenance'),
    re_path(r'^refresh_ballots_for_voters_api_v4/$',
        views_admin.refresh_ballots_for_voters_api_v4_view,
        name='refresh_ballots_for_voters_api_v4'),
    re_path(r'^retrieve_ballots_for_entire_election_api_v4/$',
        views_admin.retrieve_ballots_for_entire_election_api_v4_view,
        name='retrieve_ballots_for_entire_election_api_v4'),
    re_path(r'^retrieve_ballots_for_polling_locations_api_v4/$',
        views_admin.retrieve_ballots_for_polling_locations_api_v4_view,
        name='retrieve_ballots_for_polling_locations_api_v4'),
]
