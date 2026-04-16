# amr_domaci_1

Ovaj repozitorijum sadrži paket `amr_domaci_1` dobijen pri izradi 1. domaćeg zadatka na predmetu Autonomni mobilni roboti.

## Preduslovi

* Koristite Ubuntu 22.04 ili Ubuntu 24.04
* Instaliran ROS2; ukoliko to nije učinjeno do sad, pratiti uputstva za instalaciju [ovde](https://docs.ros.org/en/kilted/Installation.html) (ROS2 Kilted Kaiju) ako koristite Ubuntu 24.04, ili [ovde](https://docs.ros.org/en/humble/Installation.html) ako koristite Ubuntu 22.04
* Instaliran git; git se može preuzeti kucanjem narednog koda u linux terminal:
  ```
  apt-get install git
  ```

## Priprema za korišćenje paketa

Ukoliko do sada nije obavljeno, prvo je potrebno napraviti radni prostor za ROS2. U linux terminalu ukucati sledeće:

```
cd ~
mkdir ros2_ws/src
```

Sada je potrebno klonirati repozitorijum u `~/ros2_ws/src` direktorijum. U linux terminalu napisati sledeće:

```
cd ~/ros2_ws/src
git clone https://github.com/Bigulac/amr_domaci_1.git
```

Ostalo je još da se paket izbilduje. U linux terminalu iskucati sledeće:

```
cd ~/ros2_ws
colcon build --packages-select amr_domaci_1 --symlink-install
```

Opcija `--symlink-install` dozvoljava da se mogu menjati postojeće .py skripte bez potrebe ponovnog bildovanja paketa.
