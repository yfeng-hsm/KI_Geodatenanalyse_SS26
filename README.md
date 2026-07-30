# KI_Geodatenanalyse_SS26

Repository for the Summer Semester 2026 AI and geospatial data analysis module.

## lectures/

| Folder | Contents | Notebooks |
| --- | --- | --- |
| [`lectures/01_machine_learning/`](lectures/01_machine_learning/) | Machine learning basics: supervised learning, classification, clustering, model evaluation | [Exercise 1.1](lectures/01_machine_learning/notebooks/exercise_1_1_supervised_learning.ipynb), [Exercise 1.2](lectures/01_machine_learning/notebooks/exercise_1_2_classification_clustering.ipynb) |
| [`lectures/02_deep_learning/`](lectures/02_deep_learning/) | Deep learning basics: MLPs, CNNs, graph neural networks | [Exercise 2.1](lectures/02_deep_learning/notebooks/exercise_2_1_bike_sharing_mlp_pytorch.ipynb), [Exercise 2.2](lectures/02_deep_learning/notebooks/exercise_2_2_mnist_cnn_pytorch.ipynb), [Exercise 2.3](lectures/02_deep_learning/notebooks/exercise_2_3_gnn_visual_message_passing_colab.ipynb) |
| [`lectures/03_llm_basics/`](lectures/03_llm_basics/) | LLM basics and tool use with geospatial data | [Exercise 3.1](lectures/03_llm_basics/notebooks/exercise_3_1_llm_osm_tool_widget_mainz.ipynb) |
| [`lectures/04_spatial_data_analysis/`](lectures/04_spatial_data_analysis/) | Spatial data analysis and routing workflows | [Exercise 4.1](lectures/04_spatial_data_analysis/notebooks/exercise_4_1_openrouteservice_routing_mainz.ipynb) |

## llm_api/

| Notebook | API | What it does | Colab |
| --- | --- | --- | --- |
| [Testing the Uni Mainz KI-Chat API](llm_api/notebooks/uni_mainz_ki_chat_api_test.ipynb) | KI-Chat@JGU | Tests text, structured output, embeddings, and image input with the Mainz OpenAI-compatible API. | [Open in Colab](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/llm_api/notebooks/uni_mainz_ki_chat_api_test.ipynb) |
| [Testing the AcademicCloud/GWDG SAIA Chat AI API](llm_api/notebooks/academiccloud_saia_api_test.ipynb) | AcademicCloud/GWDG SAIA | Tests text, structured output, embeddings, and image input with the SAIA OpenAI-compatible API. | [Open in Colab](https://colab.research.google.com/github/yfeng-hsm/KI_Geodatenanalyse_SS26/blob/main/llm_api/notebooks/academiccloud_saia_api_test.ipynb) |

## data_loaders/

| Folder | Data | Notebook | What it does |
| --- | --- | --- | --- |
| [`data_loaders/zensus/`](data_loaders/zensus/) | Zensus 2022 100 m grid-cell data | [zensus_mainz_cells_map.ipynb](data_loaders/zensus/notebooks/zensus_mainz_cells_map.ipynb) | Downloads official grid-cell tables, extracts Mainz cells, joins indicators, and maps them. |
| [`data_loaders/airbnb/`](data_loaders/airbnb/) | Inside Airbnb Munich listings and neighbourhoods | [airbnb_munich_points.ipynb](data_loaders/airbnb/notebooks/airbnb_munich_points.ipynb) | Loads listing points, joins neighbourhood polygons, maps listings, and writes prepared GeoJSON. |
| [`data_loaders/mapillary/`](data_loaders/mapillary/) | Mapillary street-level imagery metadata | [mapillary_api_loader_mainz.ipynb](data_loaders/mapillary/notebooks/mapillary_api_loader_mainz.ipynb) | Queries image metadata around Mainz areas and maps points, thumbnails, buffers, and trajectories. |
| [`data_loaders/osm_unfall_atlas/`](data_loaders/osm_unfall_atlas/) | OpenStreetMap and German Unfallatlas accident data | Planned | Reserved for OSM road-network and accident-point loading. |
| [`data_loaders/meinrad/`](data_loaders/meinrad/) | meinRad Mainz bike-sharing snapshots | [meinrad_mainz_live_dynamic_map.ipynb](data_loaders/meinrad/notebooks/meinrad_mainz_live_dynamic_map.ipynb) | Loads committed snapshot CSVs, maps latest station availability, and creates a time-slider map. |
