==================
Full API Reference
==================
Welcome to the full API reference, here you can find the specific documentation
for every public function in PyDrake. This section of the documentation is
organised into Riot's API interfaces.

.. _pydrake_class:

The PyDrake Class
-----------------

.. autoclass:: pydrake.PyDrake
	:members:

.. _summoner_v4:

Summoner-V4
-----------

.. _league_v4:

League-V4
---------

.. _match_v4:

Match-V4
--------

.. _data_dragon:

Data Dragon
-----------

.. autoclass:: pydrake.ddragon.Champion

.. autofunction:: pydrake.ddragon.get_champion_by_id

.. _region_codes:

Supported Region Codes
----------------------
.. list-table::
	:widths: 40 40
	:header-rows: 1

	* - Region
	  - Code

	* - Brazil
	  - ``br1``
	* - Europe West
	  - ``euw1``
	* - Europe Nordic & East
	  - ``eun1``
	* - Japan
	  - ``jp1``
	* - Korea
	  - ``kr1``
	* - Latin America North
	  - ``la1``
	* - Latin America South
	  - ``la2``
	* - North America
	  - ``na``, ``na1``
	* - Oceania
	  - ``oc1``
	* - Turkey
	  - ``tr1``
	* - Russia
	  - ``ru``
	* - Public Beta
	  - ``pbe1``

.. note:: The NA region has two associated platform values - NA and NA1. Older summoners
		will have the NA platform associated with their account, while newer summoners
		will have the NA1 platform associated with their account.
