from openfisca_core.variables import Variable
from openfisca_core.periods import ETERNITY
from openfisca_core.indexed_enums import Enum
from openfisca_nsw_base.entities import Building

from openfisca_nsw_safeguard.regulation_reference import PDRS_2022

class PDRS_RF2_replace_refrigerated_cabinet_existing_equipment_is_removed(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Has the existing End User Equipment been removed?'
    metadata = {
        'alias':  'The existing equipment has been removed',
        "regulation_reference": PDRS_2022["XX", "fridge"]
    }

class PDRS_RF2_replace_refrigerated_cabinet_existing_equipment_is_legally_disposed_of(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Has the existing End User Equipment been disposed of, in accordance with legislation?'
    metadata = {
        'alias':  'The existing equipment has been removed',
        "regulation_reference": PDRS_2022["XX", "fridge"]
    }


class PDRS_RF2_replace_refrigerated_cabinet_new_equipment_is_installed_and_operating(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Is the new equipment installed and operating?'
    metadata = {
        'alias':  'The new equipment is installed and operating.',
        "regulation_reference": PDRS_2022["XX", "fridge"]
    }


class PDRS_RF2_replace_refrigerated_cabinet_meets_implementation_requirements(Variable):
    value_type = bool
    entity = Building
    definition_period = ETERNITY
    label = 'Does the new End User Equipment meet the Implementation Requirements defined in Activity Definition F1?'
    metadata = {
        'alias':  'The existing equipment is classified as a refrigerator',
        "regulation_reference": PDRS_2022["XX", "fridge"]
    }

    def formula(buildings, period, parameters):
        existing_equipment_removed = buildings('PDRS_RF2_replace_refrigerated_cabinet_existing_equipment_is_removed', period)
        existing_equipment_legally_disposed_of = buildings('PDRS_RF2_replace_refrigerated_cabinet_existing_equipment_is_legally_disposed_of', period)
        new_equipment_installed_and_operating = buildings('PDRS_RF2_replace_refrigerated_cabinet_new_equipment_is_installed_and_operating', period)
        performed_by_qualified_person = buildings('Implementation_is_performed_by_qualified_person', period)
        return(
                existing_equipment_removed *
                existing_equipment_legally_disposed_of *
                new_equipment_installed_and_operating * 
                performed_by_qualified_person
                )