##WaterPython:
**Water and Environment Tools in Python**

WaterPython aims to development of a Python library  for water and environmental engineering.
This is a free library for any use.

Collaborations and contributions to the project with new modules or functions, improvement of the existing code, are most than welcome. 

If interested, please contact or submit your Python code, with a file with the following information to be included in WaterPython blog:
* An explanation of the function to be included in the section "About" of the function page;
* A simple "sample Code" easily read;
* Finally, the expected "Result" .
* New modules water and environment can be created and included in the library.

WaterPython thank you in advance for your contribution and support.
* Get in contact with the project: http://waterpython.blogspot.com/
* Get the library at https://github.com/WaterPython
* For any question or sugestion: dmgsantos@gmail.com

Modules and functions() included in the library:

Bioreactor:
* BIO_eckenfelder_area() - area of a trickling filter according the Eckenfelder equation.
* BIO_eckenfelder_se() - downstream concentration of DBO of a trickling filter according the Eckenfelder equation.

Equipment:
* EQ_pump_p() - pump power;
* EQ_pumpstation_p(): Calculate power and total head of a pumpstation;
* EQ_pumpstation_npshr(): Calculate the required Net Positive Suction Head (NPSH) of a pumping system.
* EQ_turbine_p(): Power of a turbine.
* EQ_hydropower_p(): Power and head of a hydro-power station

Geometry:
* GEO_geometry_acircle(): Area of a full section of a circle;
* GEO_geometry_hrcircle(): Hydraulic radius of a full section of a circle;
* GEO_geometry_wpcircle(): Wet perimeter of a full section of a circle;
* GEO_geometry_aprism(): Area of a prismatic open-channel;
* GEO_geometry_wpprism(): Wet perimeter of a prismatic open-channel;
* GEO_geometry_hrprism(): Hydraulic radius of a prismatic open-channel;
* GEO_geometry_wlprism(): Width lenght of a prismatic open-channel.

Hydrology:
* HYD_kirpich_tc(): time of concentration of a river according to Kirpich equation;
* HYD_scs_ia(): initial abstraction according to SCS;
* HYD_scs_s(): Potential storage according to SCS;
* HYD_scs_cn(): Curve Number transformation according to the AMC (Antecedent Moisture Condition);
* HYD_scs_q(): Run-off according to SCS;
* HYD_scs_inf(): Infiltration according to SCS.
* HYD_scs_duh(): Synthetic Dimensionless Unit Hydrograph according to SCS.
* HYD_scs_hydrograph(): Flow hydrograph according to SCS.

PorousMediaFlow:
* PMF_darcylaw_kdarcy(): Hydraulic conductivity;
* PMF_darcylaw_q(): Darcy law specific discharge;
* PMF_darcylaw_v(): flux velocity in porous media;
* PMF_darcylaw_re(): Reynolds number of a porous media flow.

UniformFreeSurfaceFlow:
* FSF_prismatic_y() - .uniform flow heigh of a prismatic channel (rectangular, triangular, trapezoidal)
* FSF_prismatic_q() - uniform flow of a prismatic channel (rectangular, triangular, trapezoidal)

UniformPressurizedFlow:
* UPF_hw_f() - Hazen Williams friction loss;
* UPF_gms_f() - Gauckler-Manning-Strickler friction loss;
* UPF_dw_f() - Darcy-Weysbach friction loss;
* UPF_cw_f() - Colebrook-White friction loss.

WaterProperties:
* WATER_reynoldsnumber_re(): Reynolds number;
* WATER_antoine_vp(): Vapor pressure with Antoine equation;
* WATER_density_rho(): Water density;
* WATER_viscosity_dvisc(): Dynamic viscosity of water;
* WATER_viscosity_kvisc(): Kynematic viscosty of water;
* WATER_density_gamma(): Water specific weight. 

