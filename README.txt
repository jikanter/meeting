================================================
Meeting - A simple, live video app for education
================================================

This is the top level of the educational and web application components for the meeting project, a project to build a real-time, teacher-friendly webinar application.

====
Goal
====


The goal of the project is to create a collaborative environment, customizable and scalable for
content creators to do what they do best, teach content.


Welcome to development of `Meeting`. A few pointers before
digging in to the source:

The build system is a series of GNU makefiles and depends on GNU make (http://www.gnu.org/software/make/).

There are 5 servers that must be run for the project to run in it's entirety.

Here are the servers that must be run:

+--------+------------+-----------------------------+
| Server | Port (Dev) | Port (Production)           |
+========+============+=============================+
| Rails  | 3000       | 3001                        |
+--------+------------+-----------------------------+
| Django | 8000       | 8001                        |
+--------+------------+-----------------------------+
| Red5   | 5080, 5443, 1935, 8088, 1936, 9999, 9998 |
+--------+------------------------------------------+
| Aserve | 8080       | 8081                        |
+--------+------------+-----------------------------+
| Node   | 9000       | 9001                        |
+--------+------------+-----------------------------+

The red5 server can be run behind apache via the apache
java interface, which would change port 5080 to 80, however this is not necessary.

The red5 server runs the Apache OpenMeetings. 

Dependencies:
  Mariadb: 10.0.13
  Haxe: 3.1.0
  Apache OpenMeetings: 3.0.2
    imagemagick: 6.8.9
    Ghostscript: 9.14
    swftools: 0.9.2
    OpenOffice-Converter (jodconverter): 3.0-beta-4
    ffmpeg: 2.3.2
    sox: 14.4.1
  Python: 2.5
    django: 1.3
    sqlite3: 3.7.13
  nodejs: >0.10
    express.js: 3.16.6
    koa: 0.10.0
  Ruby: >1.9.3
    Rails: 3.1.1
  OpenMCL: >1.10
    Aserve: 1.2.42
      
  
Known Bugs: There is a bug when running on the localhost
with streams getting cut off.
