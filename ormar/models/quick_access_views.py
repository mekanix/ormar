"""
Contains set of fields/methods etc names that are used to bypass the checks in
NewBaseModel __getattribute__ calls to speed the calls.
"""
quick_access_set = {
    "Config",
    "model_config",
    "__cached_hash__",
    "__class__",
    "__config__",
    "__custom_root_type__",
    "__dict__",
    "__fields__",
    "__fields_set__",
    "__json_encoder__",
    "__pk_only__",
    "__post_root_validators__",
    "__pre_root_validators__",
    "__private_attributes__",
    "__same__",
    "_calculate_keys",
    "_choices_fields",
    "_convert_json",
    "_extract_db_related_names",
    "_extract_model_db_fields",
    "_extract_nested_models",
    "_extract_nested_models_from_list",
    "_extract_own_model_fields",
    "_extract_related_model_instead_of_field",
    "_get_not_excluded_fields",
    "_get_value",
    "_init_private_attributes",
    "_is_conversion_to_json_needed",
    "_iter",
    "_iterate_related_models",
    "_orm",
    "_orm_id",
    "_orm_saved",
    "_related_names",
    "_skip_ellipsis",
    "_update_and_follow",
    "_update_excluded_with_related_not_required",
    "_verify_model_can_be_initialized",
    "copy",
    "delete",
    "dict",
    "extract_related_names",
    "extract_related_fields",
    "extract_through_names",
    "update_from_dict",
    "get_child",
    "get_column_alias",
    "get_column_name_from_alias",
    "get_filtered_names_to_extract",
    "get_name",
    "get_properties",
    "get_related_field_name",
    "get_relation_model_id",
    "json",
    "keys",
    "load",
    "load_all",
    "pk_column",
    "pk_type",
    "populate_default_values",
    "prepare_model_to_save",
    "remove",
    "resolve_relation_field",
    "resolve_relation_name",
    "save",
    "save_related",
    "saved",
    "set_save_status",
    "signals",
    "translate_aliases_to_columns",
    "translate_columns_to_aliases",
    "update",
    "upsert",
}
