##!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import make_response
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():

	return '''{
  "items": [
    {
      "applier": "C10477",
      "id": 1,
      "owner": "C10477",
      "purpose": "*** RESERVED ***",
      "responsible": "C10477",
      "servername": "sv00001"
    },
    {
      "applier": "C10477",
      "id": 2,
      "owner": "C10477",
      "purpose": "*** RESERVED ***",
      "responsible": "C10477",
      "servername": "sv00002"
    },
    {
      "applier": "C10477",
      "id": 3,
      "owner": "C10477",
      "purpose": "*** RESERVED ***",
      "responsible": "C10477",
      "servername": "sv00003"
    },
    {
      "applier": "C10477",
      "id": 4,
      "owner": "C10477",
      "purpose": "*** RESERVED ***",
      "responsible": "C10477",
      "servername": "sv00004"
    },
    {
      "applier": "C10477",
      "id": 5,
      "owner": "C10477",
      "purpose": "*** RESERVED ***",
      "responsible": "C10477",
      "servername": "sv00005"
    },
    {
      "applier": "C10477",
      "id": 6,
      "owner": "C10477",
      "purpose": "*** RESERVED ***",
      "responsible": "C10477",
      "servername": "sv00006"
    },
    {
      "applier": "C10477",
      "id": 7,
      "owner": "C10477",
      "purpose": "*** RESERVED ***",
      "responsible": "C10477",
      "servername": "sv00007"
    },
    {
      "applier": "C10477",
      "id": 8,
      "owner": "C10477",
      "purpose": "*** RESERVED ***",
      "responsible": "C10477",
      "servername": "sv00008"
    },
    {
      "applier": "S13571",
      "id": 9,
      "owner": "S13571",
      "purpose": "VMware vCenter Server",
      "responsible": "S13571",
      "servername": "sv00009"
    },
    {
      "applier": "S13571",
      "id": 10,
      "owner": "S13571",
      "purpose": "VMware VUM Server",
      "responsible": "S13571",
      "servername": "sv00010"
    },
    {
      "applier": "S13571",
      "id": 11,
      "owner": "S13571",
      "purpose": "VMware vCenter Database Server",
      "responsible": "S13571",
      "servername": "sv00011"
    },
    {
      "applier": "S13571",
      "id": 12,
      "owner": "S13571",
      "purpose": "VMware Platform Service Controller vApp",
      "responsible": "S13571",
      "servername": "sv00012"
    },
    {
      "applier": "S13571",
      "id": 13,
      "owner": "S13571",
      "purpose": "VMware Platform Service Controller vApp",
      "responsible": "S13571",
      "servername": "sv00013"
    },
    {
      "applier": "S13571",
      "id": 14,
      "owner": "S13571",
      "purpose": "EMC PowerPath vApp",
      "responsible": "S13571",
      "servername": "sv00014"
    },
    {
      "applier": "S13571",
      "id": 15,
      "owner": "S13571",
      "purpose": "Element Manager Server",
      "responsible": "S13571",
      "servername": "sv00015"
    },
    {
      "applier": "S13571",
      "id": 16,
      "owner": "S13571",
      "purpose": "ESRS Server",
      "responsible": "S13571",
      "servername": "sv00016"
    },
    {
      "applier": "S13571",
      "id": 17,
      "owner": "S13571",
      "purpose": "ESRS Server",
      "responsible": "S13571",
      "servername": "sv00017"
    },
    {
      "applier": "S13571",
      "id": 18,
      "owner": "S13571",
      "purpose": "Cisco DCNM",
      "responsible": "S13571",
      "servername": "sv00018"
    },
    {
      "applier": "S13571",
      "id": 19,
      "owner": "S13571",
      "purpose": "UCS Director Server vApp",
      "responsible": "S13571",
      "servername": "sv00019"
    },
    {
      "applier": "S13571",
      "id": 20,
      "owner": "S13571",
      "purpose": "UCS Director Bare Metal Agent vApp",
      "responsible": "S13571",
      "servername": "sv00020"
    },
    {
      "applier": "S13571",
      "id": 21,
      "owner": "S13571",
      "purpose": "VMware vCenter Server",
      "responsible": "S13571",
      "servername": "sv00021"
    },
    {
      "applier": "S13571",
      "id": 22,
      "owner": "S13571",
      "purpose": "VMware VUM Server",
      "responsible": "S13571",
      "servername": "sv00022"
    },
    {
      "applier": "S13571",
      "id": 23,
      "owner": "S13571",
      "purpose": "VMware vCenter Database Server",
      "responsible": "S13571",
      "servername": "sv00023"
    },
    {
      "applier": "S13571",
      "id": 24,
      "owner": "S13571",
      "purpose": "VMware Platform Service Controller vApp",
      "responsible": "S13571",
      "servername": "sv00024"
    },
    {
      "applier": "S13571",
      "id": 25,
      "owner": "S13571",
      "purpose": "EMC PowerPath vApp",
      "responsible": "S13571",
      "servername": "sv00025"
    },
    {
      "applier": "S13571",
      "id": 26,
      "owner": "S13571",
      "purpose": "Element Manager Server",
      "responsible": "S13571",
      "servername": "sv00026"
    },
    {
      "applier": "S13571",
      "id": 27,
      "owner": "S13571",
      "purpose": "ESRS Server",
      "responsible": "S13571",
      "servername": "sv00027"
    },
    {
      "applier": "S13571",
      "id": 28,
      "owner": "S13571",
      "purpose": "ESRS Server",
      "responsible": "S13571",
      "servername": "sv00028"
    },
    {
      "applier": "S13571",
      "id": 29,
      "owner": "S13571",
      "purpose": "Cisco DCNM",
      "responsible": "S13571",
      "servername": "sv00029"
    },
    {
      "applier": "S13571",
      "id": 30,
      "owner": "S13571",
      "purpose": "UCS Director Server vApp",
      "responsible": "S13571",
      "servername": "sv00030"
    },
    {
      "applier": "S13571",
      "id": 31,
      "owner": "S13571",
      "purpose": "UCS Director Bare Metal Agent vApp",
      "responsible": "S13571",
      "servername": "sv00031"
    },
    {
      "applier": "S13571",
      "id": 32,
      "owner": "S13571",
      "purpose": "VMware Platform Service Controller vApp",
      "responsible": "S13571",
      "servername": "sv00032"
    },
    {
      "applier": "S13571",
      "id": 33,
      "owner": "S13571",
      "purpose": "VCE Vision Core Server vAPp",
      "responsible": "S13571",
      "servername": "sv00033"
    },
    {
      "applier": "S13571",
      "id": 34,
      "owner": "S13571",
      "purpose": "VCE Vision Multi-System Management",
      "responsible": "S13571",
      "servername": "sv00034"
    },
    {
      "applier": "S13571",
      "id": 35,
      "owner": "S13571",
      "purpose": "Vision Multi Site Prepositioning ",
      "responsible": "S13571",
      "servername": "sv00035"
    },
    {
      "applier": "S13571",
      "id": 36,
      "owner": "S13571",
      "purpose": "VCE Vision Core Server  vApp",
      "responsible": "S13571",
      "servername": "sv00036"
    },
    {
      "applier": "S13571",
      "id": 37,
      "owner": "S13571",
      "purpose": "VCE Vision Multi-System Management",
      "responsible": "S13571",
      "servername": "sv00037"
    },
    {
      "applier": "S13571",
      "id": 38,
      "owner": "S13571",
      "purpose": "Vision Multi Site Prepositioning ",
      "responsible": "S13571",
      "servername": "sv00038"
    },
    {
      "applier": "A1912",
      "id": 39,
      "owner": "D12390",
      "purpose": "Server f\u00c3\u00bcr elektronisches AES System",
      "responsible": "A1912",
      "servername": "sv00039"
    },
    {
      "applier": "L9749",
      "id": 40,
      "owner": "E10215",
      "purpose": "LogIS Server CSC",
      "responsible": "L9749",
      "servername": "sv00040"
    },
    {
      "applier": "A1912",
      "id": 41,
      "owner": "C0930",
      "purpose": "Edis Web Server",
      "responsible": "A1912",
      "servername": "sv00041"
    },
    {
      "applier": "A1912",
      "id": 42,
      "owner": "S19285",
      "purpose": "SQL DB Server",
      "responsible": "A1912",
      "servername": "sv00042"
    },
    {
      "applier": "L9749",
      "id": 43,
      "owner": "B6833",
      "purpose": "ITSM SM-App-1-Int",
      "responsible": "L9749",
      "servername": "sv00043"
    },
    {
      "applier": "L9749",
      "id": 44,
      "owner": "B6833",
      "purpose": "ITSM SM-App-2-Int",
      "responsible": "L9749",
      "servername": "sv00044"
    },
    {
      "applier": "L9749",
      "id": 45,
      "owner": "B6833",
      "purpose": "ITSM SM-LB-Int",
      "responsible": "L9749",
      "servername": "sv00045"
    },
    {
      "applier": "L9749",
      "id": 46,
      "owner": "B6833",
      "purpose": "UCMDB-App-Int",
      "responsible": "L9749",
      "servername": "sv00046"
    },
    {
      "applier": "L9749",
      "id": 47,
      "owner": "B6833",
      "purpose": "UCMDB-Probe-Int",
      "responsible": "L9749",
      "servername": "sv00047"
    },
    {
      "applier": "L9749",
      "id": 48,
      "owner": "B6833",
      "purpose": "SM-Web-1-Int",
      "responsible": "L9749",
      "servername": "sv00048"
    },
    {
      "applier": "L9749",
      "id": 49,
      "owner": "B6833",
      "purpose": "SM-Web-2-Int",
      "responsible": "L9749",
      "servername": "sv00049"
    },
    {
      "applier": "L9749",
      "id": 50,
      "owner": "B6833",
      "purpose": "SM-Src-1-Int",
      "responsible": "L9749",
      "servername": "sv00050"
    },
    {
      "applier": "L9749",
      "id": 51,
      "owner": "B6833",
      "purpose": "SM-Src-2-Int",
      "responsible": "L9749",
      "servername": "sv00051"
    },
    {
      "applier": "L9749",
      "id": 52,
      "owner": "B6833",
      "purpose": "SM-Mob-Int",
      "responsible": "L9749",
      "servername": "sv00052"
    },
    {
      "applier": "L9749",
      "id": 53,
      "owner": "B6833",
      "purpose": "SM-SmA_IDOL-Int",
      "responsible": "L9749",
      "servername": "sv00053"
    },
    {
      "applier": "L9749",
      "id": 54,
      "owner": "B6833",
      "purpose": "SM-SmA_Image-Int",
      "responsible": "L9749",
      "servername": "sv00054"
    },
    {
      "applier": "L9749",
      "id": 55,
      "owner": "B6833",
      "purpose": "SM-KM-Int",
      "responsible": "L9749",
      "servername": "sv00055"
    },
    {
      "applier": "L9749",
      "id": 56,
      "owner": "B6833",
      "purpose": "SM-CIT-Int",
      "responsible": "L9749",
      "servername": "sv00056"
    },
    {
      "applier": "L9749",
      "id": 57,
      "owner": "B6833",
      "purpose": "OO-App-1-Int",
      "responsible": "L9749",
      "servername": "sv00057"
    },
    {
      "applier": "L9749",
      "id": 58,
      "owner": "B6833",
      "purpose": "OO-App-2-Int",
      "responsible": "L9749",
      "servername": "sv00058"
    },
    {
      "applier": "A1912",
      "id": 59,
      "owner": "A22929",
      "purpose": "ESX Host",
      "responsible": "A1912",
      "servername": "sv00059"
    },
    {
      "applier": "A1912",
      "id": 60,
      "owner": "A22929",
      "purpose": "ESX Host",
      "responsible": "A1912",
      "servername": "sv00060"
    },
    {
      "applier": "A1912",
      "id": 61,
      "owner": "A22929",
      "purpose": "ESX Host",
      "responsible": "A1912",
      "servername": "sv00061"
    },
    {
      "applier": "A1912",
      "id": 62,
      "owner": "A22929",
      "purpose": "ESX Host",
      "responsible": "A1912",
      "servername": "sv00062"
    },
    {
      "applier": "A1912",
      "id": 63,
      "owner": "A22929",
      "purpose": "ESX Host",
      "responsible": "A1912",
      "servername": "sv00063"
    },
    {
      "applier": "A1912",
      "id": 64,
      "owner": "A22929",
      "purpose": "ESX Host",
      "responsible": "A1912",
      "servername": "sv00064"
    },
    {
      "applier": "A1912",
      "id": 65,
      "owner": "A22929",
      "purpose": "Storage ESX local",
      "responsible": "A1912",
      "servername": "sv00065"
    },
    {
      "applier": "A1912",
      "id": 66,
      "owner": "C0930",
      "purpose": "Edis Web Server",
      "responsible": "A1912",
      "servername": "sv00066"
    },
    {
      "applier": "A1912",
      "id": 67,
      "owner": "S19285",
      "purpose": "SQL DB Server",
      "responsible": "A1912",
      "servername": "sv00067"
    },
    {
      "applier": "L9749",
      "id": 68,
      "owner": "E10215",
      "purpose": "LogIS Server CSC",
      "responsible": "L9749",
      "servername": "sv00068"
    },
    {
      "applier": "L9749",
      "id": 69,
      "owner": "B6833",
      "purpose": "SM-App-1-Int",
      "responsible": "L9749",
      "servername": "sv00069"
    },
    {
      "applier": "L9749",
      "id": 70,
      "owner": "B6833",
      "purpose": "SM-App-2-Int",
      "responsible": "L9749",
      "servername": "sv00070"
    },
    {
      "applier": "L9749",
      "id": 71,
      "owner": "B6833",
      "purpose": "SM-LB-Int",
      "responsible": "L9749",
      "servername": "sv00071"
    },
    {
      "applier": "L9749",
      "id": 72,
      "owner": "B6833",
      "purpose": "UCMDB-App-Int",
      "responsible": "L9749",
      "servername": "sv00072"
    },
    {
      "applier": "L9749",
      "id": 73,
      "owner": "L9749",
      "purpose": "UCMDB-Probe-Int",
      "responsible": "L9749",
      "servername": "sv00073"
    },
    {
      "applier": "L9749",
      "id": 74,
      "owner": "B6833",
      "purpose": "SM-Web-1-Int",
      "responsible": "L9749",
      "servername": "sv00074"
    },
    {
      "applier": "L9749",
      "id": 75,
      "owner": "B6833",
      "purpose": "SM-Web-2-Int",
      "responsible": "L9749",
      "servername": "sv00075"
    },
    {
      "applier": "L9749",
      "id": 76,
      "owner": "B6833",
      "purpose": "SM-Src-1-Int",
      "responsible": "L9749",
      "servername": "sv00076"
    },
    {
      "applier": "L9749",
      "id": 77,
      "owner": "B6833",
      "purpose": "SM-Src-2-Int",
      "responsible": "L9749",
      "servername": "sv00077"
    },
    {
      "applier": "L9749",
      "id": 78,
      "owner": "B6833",
      "purpose": "SM-Mob-Int",
      "responsible": "L9749",
      "servername": "sv00078"
    },
    {
      "applier": "L9749",
      "id": 79,
      "owner": "B6833",
      "purpose": "SM-SmA_IDOL-Int",
      "responsible": "L9749",
      "servername": "sv00079"
    },
    {
      "applier": "L9749",
      "id": 80,
      "owner": "B6833",
      "purpose": "SM-SmA_Image-Int",
      "responsible": "L9749",
      "servername": "sv00080"
    },
    {
      "applier": "L9749",
      "id": 81,
      "owner": "B6833",
      "purpose": "SM-KM-Int",
      "responsible": "L9749",
      "servername": "sv00081"
    },
    {
      "applier": "L9749",
      "id": 82,
      "owner": "B6833",
      "purpose": "SM-CIT-Int",
      "responsible": "L9749",
      "servername": "sv00082"
    },
    {
      "applier": "L9749",
      "id": 83,
      "owner": "C0930",
      "purpose": "Edis Web Server",
      "responsible": "A1912",
      "servername": "sv00083"
    },
    {
      "applier": "L9749",
      "id": 84,
      "owner": "S19285",
      "purpose": "SQL DB Server",
      "responsible": "A1912",
      "servername": "sv00084"
    },
    {
      "applier": "K15717",
      "id": 85,
      "owner": "J3765",
      "purpose": "Terminal Server",
      "responsible": "K15717",
      "servername": "sv00085"
    },
    {
      "applier": "k15717",
      "id": 86,
      "owner": "J3765",
      "purpose": "AspenTech IP.21 Server",
      "responsible": "K15717",
      "servername": "sv00086"
    },
    {
      "applier": "L9749",
      "id": 87,
      "owner": "B6833",
      "purpose": "SM-SmA_IDOL-Dev2",
      "responsible": "L9749",
      "servername": "sv00087"
    },
    {
      "applier": "L9749",
      "id": 88,
      "owner": "C5256",
      "purpose": "Office Empower Search ",
      "responsible": "L9749",
      "servername": "sv00088"
    },
    {
      "applier": "A1912",
      "id": 89,
      "owner": "D12390",
      "purpose": "Server f\u00c3\u00bcr elektronisches AES System",
      "responsible": "A1912",
      "servername": "sv00089"
    },
    {
      "applier": "L9749",
      "id": 90,
      "owner": "B1570",
      "purpose": "WEKAMedia Arbeitsschutz360plus",
      "responsible": "L9749",
      "servername": "sv00090"
    },
    {
      "applier": "G12866",
      "id": 91,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "G12866",
      "servername": "sv00091"
    },
    {
      "applier": "G12866",
      "id": 92,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "G12866",
      "servername": "sv00092"
    },
    {
      "applier": "G12866",
      "id": 93,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "G12866",
      "servername": "sv00093"
    },
    {
      "applier": "G12866",
      "id": 94,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "G12866",
      "servername": "sv00094"
    },
    {
      "applier": "L9749",
      "id": 95,
      "owner": "F1768",
      "purpose": "SQL Server",
      "responsible": "L9749",
      "servername": "sv00095"
    },
    {
      "applier": "A1912",
      "id": 96,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "A1912",
      "servername": "sv00096"
    },
    {
      "applier": "A1912",
      "id": 97,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "A1912",
      "servername": "sv00097"
    },
    {
      "applier": "A1912",
      "id": 98,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "A1912",
      "servername": "sv00098"
    },
    {
      "applier": "A1912",
      "id": 99,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "A1912",
      "servername": "sv00099"
    },
    {
      "applier": "A1912",
      "id": 100,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "A1912",
      "servername": "sv00100"
    },
    {
      "applier": "A1912",
      "id": 101,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "A1912",
      "servername": "sv00101"
    },
    {
      "applier": "A1912",
      "id": 102,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "A1912",
      "servername": "sv00102"
    },
    {
      "applier": "A1912",
      "id": 103,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "A1912",
      "servername": "sv00103"
    },
    {
      "applier": "A1912",
      "id": 104,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "A1912",
      "servername": "sv00104"
    },
    {
      "applier": "A1912",
      "id": 105,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "A1912",
      "servername": "sv00105"
    },
    {
      "applier": "A1912",
      "id": 106,
      "owner": "S20376",
      "purpose": "APP Server WPB QA (WAS-4600)",
      "responsible": "A1912",
      "servername": "sv00106"
    },
    {
      "applier": "L9749",
      "id": 107,
      "owner": "F8735",
      "purpose": "IBM Connection File Viewer",
      "responsible": "L9749",
      "servername": "sv00107"
    },
    {
      "applier": "L9749",
      "id": 108,
      "owner": "F8735",
      "purpose": "IBM Connection File Viewer",
      "responsible": "L9749",
      "servername": "sv00108"
    },
    {
      "applier": "L9749",
      "id": 109,
      "owner": "F8735",
      "purpose": "IBM Connection Server",
      "responsible": "L9749",
      "servername": "sv00109"
    },
    {
      "applier": "L9749",
      "id": 110,
      "owner": "F8735",
      "purpose": "IBM Connection Server",
      "responsible": "L9749",
      "servername": "sv00110"
    },
    {
      "applier": "L9749",
      "id": 111,
      "owner": "F8735",
      "purpose": "IBM Connection Server",
      "responsible": "L9749",
      "servername": "sv00111"
    },
    {
      "applier": "L9749",
      "id": 112,
      "owner": "F8735",
      "purpose": "IBM Connection Server",
      "responsible": "L9749",
      "servername": "sv00112"
    },
    {
      "applier": "L9749",
      "id": 113,
      "owner": "F8735",
      "purpose": "IBM Cognos Metrics Server",
      "responsible": "L9749",
      "servername": "sv00113"
    },
    {
      "applier": "L9749",
      "id": 114,
      "owner": "F8735",
      "purpose": "IBM Cognos Metrics Server",
      "responsible": "L9749",
      "servername": "sv00114"
    },
    {
      "applier": "A1912",
      "id": 115,
      "owner": "O1854",
      "purpose": "ASP Terminal Server Darmstadt",
      "responsible": "A1912",
      "servername": "sv00115"
    },
    {
      "applier": "A1912",
      "id": 116,
      "owner": "O1854",
      "purpose": "ASP Terminal Server Darmstadt",
      "responsible": "A1912",
      "servername": "sv00116"
    },
    {
      "applier": "A1912",
      "id": 117,
      "owner": "S20376",
      "purpose": "APP Server Process Mining (WAS-5000)",
      "responsible": "A1912",
      "servername": "sv00117"
    },
    {
      "applier": "I0378",
      "id": 118,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "I0378",
      "servername": "sv00118"
    },
    {
      "applier": "I0378",
      "id": 119,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "I0378",
      "servername": "sv00119"
    },
    {
      "applier": "A0423",
      "id": 120,
      "owner": "M27992",
      "purpose": "Softgate Server",
      "responsible": "A0423",
      "servername": "sv00120"
    },
    {
      "applier": "A0423",
      "id": 121,
      "owner": "M27992",
      "purpose": "Softgate Server",
      "responsible": "A0423",
      "servername": "sv00121"
    },
    {
      "applier": "A1912",
      "id": 122,
      "owner": "K0962",
      "purpose": "Applikationsserver AY-DA",
      "responsible": "A1912",
      "servername": "sv00122"
    },
    {
      "applier": "D15437",
      "id": 123,
      "owner": "D15437",
      "purpose": "O1854",
      "responsible": "D15437",
      "servername": "sv00123"
    },
    {
      "applier": "D15437",
      "id": 124,
      "owner": "O1854",
      "purpose": "Special APP ASP-Server",
      "responsible": "D15437",
      "servername": "sv00124"
    },
    {
      "applier": "D15437",
      "id": 125,
      "owner": "O1854",
      "purpose": "Special APP ASP-Server",
      "responsible": "D15437",
      "servername": "sv00125"
    },
    {
      "applier": "D15437",
      "id": 126,
      "owner": "O1854",
      "purpose": "Special APP ASP-Server",
      "responsible": "D15437",
      "servername": "sv00126"
    },
    {
      "applier": "L9749",
      "id": 127,
      "owner": "F9212",
      "purpose": "ELO IndexServer",
      "responsible": "L9749",
      "servername": "sv00127"
    },
    {
      "applier": "L9749",
      "id": 128,
      "owner": "B6833",
      "purpose": "ITSM ALM-DEV2",
      "responsible": "L9749",
      "servername": "sv00128"
    },
    {
      "applier": "D7982",
      "id": 129,
      "owner": "T0389",
      "purpose": "Dokuware",
      "responsible": "D7982",
      "servername": "sv00129"
    },
    {
      "applier": "L9749",
      "id": 130,
      "owner": "B6833",
      "purpose": "ITSM QA2-AM-Web",
      "responsible": "L9749",
      "servername": "sv00130"
    },
    {
      "applier": "L9749",
      "id": 131,
      "owner": "B6833",
      "purpose": "ITSM QA2-AM-App",
      "responsible": "L9749",
      "servername": "sv00131"
    },
    {
      "applier": "O0067",
      "id": 132,
      "owner": "B6833",
      "purpose": "ITSM AM-WEB1-QA",
      "responsible": "O0067",
      "servername": "sv00132"
    },
    {
      "applier": "O0067",
      "id": 133,
      "owner": "B6833",
      "purpose": "ITSM AM-WEB2-QA",
      "responsible": "O0067",
      "servername": "sv00133"
    },
    {
      "applier": "O0067",
      "id": 134,
      "owner": "B6833",
      "purpose": "ITSM AM-APP1-QA",
      "responsible": "O0067",
      "servername": "sv00134"
    },
    {
      "applier": "O0067",
      "id": 135,
      "owner": "B6833",
      "purpose": "ITSM AM-APP2-QA",
      "responsible": "O0067",
      "servername": "sv00135"
    },
    {
      "applier": "O0067",
      "id": 136,
      "owner": "B6833",
      "purpose": "ITSM AM-WEB1-PROD",
      "responsible": "O0067",
      "servername": "sv00136"
    },
    {
      "applier": "O0067",
      "id": 137,
      "owner": "B6833",
      "purpose": "ITSM AM-WEB2-PROD",
      "responsible": "O0067",
      "servername": "sv00137"
    },
    {
      "applier": "O0067",
      "id": 138,
      "owner": "B6833",
      "purpose": "ITSM AM-APP1-PROD",
      "responsible": "O0067",
      "servername": "sv00138"
    },
    {
      "applier": "O0067",
      "id": 139,
      "owner": "B6833",
      "purpose": "ITSM AM-APP2-PROD",
      "responsible": "O0067",
      "servername": "sv00139"
    },
    {
      "applier": "L9749",
      "id": 140,
      "owner": "J0626",
      "purpose": "DLS IP-Phones for Team UCT",
      "responsible": "L9749",
      "servername": "sv00140"
    },
    {
      "applier": "G12866",
      "id": 141,
      "owner": "J0559",
      "purpose": "ASP Terminal Server",
      "responsible": "G12866",
      "servername": "sv00141"
    },
    {
      "applier": "H1863",
      "id": 142,
      "owner": "J0559",
      "purpose": "ASP Terminal Server (eDesk Core Server)",
      "responsible": "H1863",
      "servername": "sv00142"
    },
    {
      "applier": "H1863",
      "id": 143,
      "owner": "J0559",
      "purpose": "ASP Terminal Server (eDesk Core Server)",
      "responsible": "H1863",
      "servername": "sv00143"
    },
    {
      "applier": "H1863",
      "id": 144,
      "owner": "J0559",
      "purpose": "ASP Terminal Server (eDesk Core Server)",
      "responsible": "H1863",
      "servername": "sv00144"
    },
    {
      "applier": "H1863",
      "id": 145,
      "owner": "J0559",
      "purpose": "ASP Terminal Server (eDesk Core Server)",
      "responsible": "H1863",
      "servername": "sv00145"
    },
    {
      "applier": "H1863",
      "id": 146,
      "owner": "J0559",
      "purpose": "ASP Terminal Server (eDesk Core Server)",
      "responsible": "H1863",
      "servername": "sv00146"
    },
    {
      "applier": "H1863",
      "id": 147,
      "owner": "J0559",
      "purpose": "ASP Terminal Server (eDesk Core Server)",
      "responsible": "H1863",
      "servername": "sv00147"
    },
    {
      "applier": "L9749",
      "id": 148,
      "owner": "F9212",
      "purpose": "ELO IndexServer",
      "responsible": "L9749",
      "servername": "sv00148"
    },
    {
      "applier": "L9749",
      "id": 149,
      "owner": "T0389",
      "purpose": "Talent Managemet Server",
      "responsible": "L9749",
      "servername": "sv00149"
    },
    {
      "applier": "J0649",
      "id": 150,
      "owner": "O1854",
      "purpose": "ASP-Terminalserver",
      "responsible": "J0649",
      "servername": "sv00150"
    },
    {
      "applier": "J0649",
      "id": 151,
      "owner": "O1854",
      "purpose": "ASP-Terminalserver",
      "responsible": "J0649",
      "servername": "sv00151"
    },
    {
      "applier": "J0649",
      "id": 152,
      "owner": "O1854",
      "purpose": "ASP-Terminalserver",
      "responsible": "J0649",
      "servername": "sv00152"
    },
    {
      "applier": "J0649",
      "id": 153,
      "owner": "O1854",
      "purpose": "ASP-Terminalserver",
      "responsible": "J0649",
      "servername": "sv00153"
    },
    {
      "applier": "J0649",
      "id": 154,
      "owner": "O1854",
      "purpose": "ASP-Terminalserver",
      "responsible": "J0649",
      "servername": "sv00154"
    },
    {
      "applier": "J0649",
      "id": 155,
      "owner": "O1854",
      "purpose": "ASP-Terminalserver",
      "responsible": "J0649",
      "servername": "sv00155"
    },
    {
      "applier": "J0649",
      "id": 156,
      "owner": "O1854",
      "purpose": "ASP-Terminalserver",
      "responsible": "J0649",
      "servername": "sv00156"
    },
    {
      "applier": "J0649",
      "id": 157,
      "owner": "O1854",
      "purpose": "ASP-Terminalserver",
      "responsible": "J0649",
      "servername": "sv00157"
    },
    {
      "applier": "D15437",
      "id": 158,
      "owner": "O1854",
      "purpose": "ASP Terminal Server RFN",
      "responsible": "D15437",
      "servername": "sv00158"
    },
    {
      "applier": "D15437",
      "id": 159,
      "owner": "O1854",
      "purpose": "ASP Terminal Server RFN",
      "responsible": "D15437",
      "servername": "sv00159"
    },
    {
      "applier": "D15437",
      "id": 160,
      "owner": "O1854",
      "purpose": "ASP Terminal Server RFN",
      "responsible": "D15437",
      "servername": "sv00160"
    },
    {
      "applier": "D15437",
      "id": 161,
      "owner": "O1854",
      "purpose": "ASP Terminal Server RFN",
      "responsible": "D15437",
      "servername": "sv00161"
    },
    {
      "applier": "A1912",
      "id": 162,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server Marl",
      "responsible": "A1912",
      "servername": "sv00162"
    },
    {
      "applier": "A1912",
      "id": 163,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server Marl",
      "responsible": "A1912",
      "servername": "sv00163"
    },
    {
      "applier": "A1912",
      "id": 164,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server Marl",
      "responsible": "A1912",
      "servername": "sv00164"
    },
    {
      "applier": "A1912",
      "id": 165,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server Marl",
      "responsible": "A1912",
      "servername": "sv00165"
    },
    {
      "applier": "A1912",
      "id": 166,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server Marl",
      "responsible": "A1912",
      "servername": "sv00166"
    },
    {
      "applier": "I0378",
      "id": 167,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server ANT",
      "responsible": "I0378",
      "servername": "sv00167"
    },
    {
      "applier": "I0378",
      "id": 168,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server ANT",
      "responsible": "I0378",
      "servername": "sv00168"
    },
    {
      "applier": "S18344",
      "id": 169,
      "owner": "B1662",
      "purpose": "CyberArk Project - Primary Vault",
      "responsible": "S18344",
      "servername": "sv00169"
    },
    {
      "applier": "S18344",
      "id": 170,
      "owner": "B1662",
      "purpose": "CyberArk Project - Secondary Vault",
      "responsible": "S18344",
      "servername": "sv00170"
    },
    {
      "applier": "S18344",
      "id": 171,
      "owner": "B1662",
      "purpose": "CyberArk Project - CPM",
      "responsible": "S18344",
      "servername": "sv00171"
    },
    {
      "applier": "S18344",
      "id": 172,
      "owner": "B1662",
      "purpose": "CyberArk Project - PVWA",
      "responsible": "S18344",
      "servername": "sv00172"
    },
    {
      "applier": "D15437",
      "id": 173,
      "owner": "D15437",
      "purpose": "ESX Host RFN",
      "responsible": "D15437",
      "servername": "sv00173"
    },
    {
      "applier": "D15437",
      "id": 174,
      "owner": "D15437",
      "purpose": "ESX Host RFN",
      "responsible": "D15437",
      "servername": "sv00174"
    },
    {
      "applier": "D15437",
      "id": 175,
      "owner": "D15437",
      "purpose": "ESX Host RFN",
      "responsible": "D15437",
      "servername": "sv00175"
    },
    {
      "applier": "D15437",
      "id": 176,
      "owner": "D15437",
      "purpose": "ESX Host RFN",
      "responsible": "D15437",
      "servername": "sv00176"
    },
    {
      "applier": "L9749",
      "id": 177,
      "owner": "B6833",
      "purpose": "ITSM ALM-DEV2",
      "responsible": "L9749",
      "servername": "sv00177"
    },
    {
      "applier": "O0067",
      "id": 178,
      "owner": "C11917",
      "purpose": "ITSM AM-APP1-PROD",
      "responsible": "O0067",
      "servername": "sv00178"
    },
    {
      "applier": "O0067",
      "id": 179,
      "owner": "C11917",
      "purpose": "TestServer Mcafee MAR (Active Response Server)",
      "responsible": "O0067",
      "servername": "sv00179"
    },
    {
      "applier": "L9749",
      "id": 180,
      "owner": "M33751",
      "purpose": "MobileIron Appliances Core",
      "responsible": "L9749",
      "servername": "sv00180"
    },
    {
      "applier": "L9749",
      "id": 181,
      "owner": "A2356",
      "purpose": " WSUS 4/CM Software Update Server",
      "responsible": "L9749",
      "servername": "sv00181"
    },
    {
      "applier": "A1912",
      "id": 182,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server ESR",
      "responsible": "A1912",
      "servername": "sv00182"
    },
    {
      "applier": "A1912",
      "id": 183,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server ESR",
      "responsible": "A1912",
      "servername": "sv00183"
    },
    {
      "applier": "L9749",
      "id": 184,
      "owner": "A0751",
      "purpose": "OnTime TeamKalender",
      "responsible": "L9749",
      "servername": "sv00184"
    },
    {
      "applier": "L9749",
      "id": 185,
      "owner": "F1768",
      "purpose": "SQL Server Reporting Services QA",
      "responsible": "L9749",
      "servername": "sv00185"
    },
    {
      "applier": "L9749",
      "id": 186,
      "owner": "F1768",
      "purpose": "SQL Admin Server",
      "responsible": "L9749",
      "servername": "sv00186"
    },
    {
      "applier": "L9749",
      "id": 187,
      "owner": "M33751",
      "purpose": "MobileIron Appliance Core",
      "responsible": "L9749",
      "servername": "sv00187"
    },
    {
      "applier": "L9749",
      "id": 188,
      "owner": "M33751",
      "purpose": "MobileIron Appliance Sentry",
      "responsible": "L9749",
      "servername": "sv00188"
    },
    {
      "applier": "L9749",
      "id": 189,
      "owner": "M33751",
      "purpose": "MobileIron Appliance Sentry",
      "responsible": "L9749",
      "servername": "sv00189"
    },
    {
      "applier": "L9749",
      "id": 190,
      "owner": "S0344",
      "purpose": "ESRS Policy Manager",
      "responsible": "L9749",
      "servername": "sv00190"
    },
    {
      "applier": "S18344",
      "id": 191,
      "owner": "S0344",
      "purpose": "ESRS Po0licy Manager",
      "responsible": "S18344",
      "servername": "sv00191"
    },
    {
      "applier": "L9749",
      "id": 192,
      "owner": "G0179",
      "purpose": "Exchange QA Server",
      "responsible": "L9749",
      "servername": "sv00192"
    },
    {
      "applier": "L9749",
      "id": 193,
      "owner": "G0179",
      "purpose": "Exchange Applikation Server",
      "responsible": "L9749",
      "servername": "sv00193"
    },
    {
      "applier": "L9749",
      "id": 194,
      "owner": "G0179",
      "purpose": "Exchange Admin Server",
      "responsible": "L9749",
      "servername": "sv00194"
    },
    {
      "applier": "L9749",
      "id": 195,
      "owner": "D5516",
      "purpose": "RICOH Remote Connector",
      "responsible": "L9749",
      "servername": "sv00195"
    },
    {
      "applier": "B13131",
      "id": 196,
      "owner": "B13131",
      "purpose": "Jump Server",
      "responsible": "B13131",
      "servername": "sv00196"
    },
    {
      "applier": "L9749",
      "id": 197,
      "owner": "O1854",
      "purpose": "ASP HW Terminalserver",
      "responsible": "L9749",
      "servername": "sv00197"
    },
    {
      "applier": "L9749",
      "id": 198,
      "owner": "O1854",
      "purpose": "ASP HW Terminalserver",
      "responsible": "L9749",
      "servername": "sv00198"
    },
    {
      "applier": "A1912",
      "id": 199,
      "owner": "H1863",
      "purpose": "VM Jump Server Marl",
      "responsible": "A1912",
      "servername": "sv00199"
    },
    {
      "applier": "L9749",
      "id": 200,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server",
      "responsible": "L9749",
      "servername": "sv00200"
    },
    {
      "applier": "L9749",
      "id": 201,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server",
      "responsible": "L9749",
      "servername": "sv00201"
    },
    {
      "applier": "L9749",
      "id": 202,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server",
      "responsible": "L9749",
      "servername": "sv00202"
    },
    {
      "applier": "L9749",
      "id": 203,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server",
      "responsible": "L9749",
      "servername": "sv00203"
    },
    {
      "applier": "L9749",
      "id": 204,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server",
      "responsible": "L9749",
      "servername": "sv00204"
    },
    {
      "applier": "L9749",
      "id": 205,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server",
      "responsible": "L9749",
      "servername": "sv00205"
    },
    {
      "applier": "L9749",
      "id": 206,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server",
      "responsible": "L9749",
      "servername": "sv00206"
    },
    {
      "applier": "L9749",
      "id": 207,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server",
      "responsible": "L9749",
      "servername": "sv00207"
    },
    {
      "applier": "L9749",
      "id": 208,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server",
      "responsible": "L9749",
      "servername": "sv00208"
    },
    {
      "applier": "L9749",
      "id": 209,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server",
      "responsible": "L9749",
      "servername": "sv00209"
    },
    {
      "applier": "L9749",
      "id": 210,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server",
      "responsible": "L9749",
      "servername": "sv00210"
    },
    {
      "applier": "L9749",
      "id": 211,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server",
      "responsible": "L9749",
      "servername": "sv00211"
    },
    {
      "applier": "L9749",
      "id": 212,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server",
      "responsible": "L9749",
      "servername": "sv00212"
    },
    {
      "applier": "L9749",
      "id": 213,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server",
      "responsible": "L9749",
      "servername": "sv00213"
    },
    {
      "applier": "L9749",
      "id": 214,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server",
      "responsible": "L9749",
      "servername": "sv00214"
    },
    {
      "applier": "L9749",
      "id": 215,
      "owner": "O1854",
      "purpose": "ASP HW Terminal Server",
      "responsible": "L9749",
      "servername": "sv00215"
    },
    {
      "applier": "L9749",
      "id": 216,
      "owner": "C11917",
      "purpose": "ArcSight Logger Server",
      "responsible": "L9749",
      "servername": "sv00216"
    },
    {
      "applier": "L9749",
      "id": 217,
      "owner": "C11917",
      "purpose": "ArcSight Logger Server",
      "responsible": "L9749",
      "servername": "sv00217"
    },
    {
      "applier": "L9749",
      "id": 218,
      "owner": "C11917",
      "purpose": "ArcSight Logger Server",
      "responsible": "L9749",
      "servername": "sv00218"
    },
    {
      "applier": "L9749",
      "id": 219,
      "owner": "C11917",
      "purpose": "ArcSight Logger Server",
      "responsible": "L9749",
      "servername": "sv00219"
    },
    {
      "applier": "L9749",
      "id": 220,
      "owner": "C11917",
      "purpose": "ArcSight Logger Server",
      "responsible": "L9749",
      "servername": "sv00220"
    },
    {
      "applier": "L9749",
      "id": 221,
      "owner": "C11917",
      "purpose": "ArcSight Logger Server",
      "responsible": "L9749",
      "servername": "sv00221"
    },
    {
      "applier": "L9749",
      "id": 222,
      "owner": "C11917",
      "purpose": "ArcSight Logger Server",
      "responsible": "L9749",
      "servername": "sv00222"
    },
    {
      "applier": "L9749",
      "id": 223,
      "owner": "C11917",
      "purpose": "ArcSight Logger Server",
      "responsible": "L9749",
      "servername": "sv00223"
    },
    {
      "applier": "L9749",
      "id": 224,
      "owner": "C11917",
      "purpose": "ArcSight Logger Server",
      "responsible": "L9749",
      "servername": "sv00224"
    },
    {
      "applier": "L9749",
      "id": 225,
      "owner": "C11917",
      "purpose": "ArcSight Logger Server",
      "responsible": "L9749",
      "servername": "sv00225"
    },
    {
      "applier": "L9749",
      "id": 226,
      "owner": "C11917",
      "purpose": "ArcSight Logger Server",
      "responsible": "L9749",
      "servername": "sv00226"
    },
    {
      "applier": "L9749",
      "id": 227,
      "owner": "C11917",
      "purpose": "ArcSight Loadbalancer",
      "responsible": "L9749",
      "servername": "sv00227"
    },
    {
      "applier": "L9749",
      "id": 228,
      "owner": "C11917",
      "purpose": "ArcSight Management Center",
      "responsible": "L9749",
      "servername": "sv00228"
    },
    {
      "applier": "L9749",
      "id": 229,
      "owner": "C11917",
      "purpose": "ArcSight Connector Server",
      "responsible": "L9749",
      "servername": "sv00229"
    },
    {
      "applier": "L9749",
      "id": 230,
      "owner": "C11917",
      "purpose": "ArcSight Connector Server",
      "responsible": "L9749",
      "servername": "sv00230"
    },
    {
      "applier": "L9749",
      "id": 231,
      "owner": "C11917",
      "purpose": "ArcSight Connector Server",
      "responsible": "L9749",
      "servername": "sv00231"
    },
    {
      "applier": "L9749",
      "id": 232,
      "owner": "N5882",
      "purpose": "Nexthink for Servicedesk test",
      "responsible": "L9749",
      "servername": "sv00232"
    },
    {
      "applier": "B13131",
      "id": 233,
      "owner": "B13131",
      "purpose": "Datacenter File Server",
      "responsible": "B13131",
      "servername": "sv00233"
    },
    {
      "applier": "L9749",
      "id": 234,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "L9749",
      "servername": "sv00234"
    },
    {
      "applier": "L9749",
      "id": 235,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "L9749",
      "servername": "sv00235"
    },
    {
      "applier": "L9749",
      "id": 236,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "L9749",
      "servername": "sv00236"
    },
    {
      "applier": "L9749",
      "id": 237,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "L9749",
      "servername": "sv00237"
    },
    {
      "applier": "L9749",
      "id": 238,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "L9749",
      "servername": "sv00238"
    },
    {
      "applier": "L9749",
      "id": 239,
      "owner": "O1854",
      "purpose": "ASP Terminal server",
      "responsible": "L9749",
      "servername": "sv00239"
    },
    {
      "applier": "L9749",
      "id": 240,
      "owner": "A1019",
      "purpose": "Mobile Devices Mgmt BES12  Samsung/IOS ",
      "responsible": "L9749",
      "servername": "sv00240"
    },
    {
      "applier": "L9749",
      "id": 241,
      "owner": "A1019",
      "purpose": "Mobile Devices Mgmt BES12  Samsung/IOS ",
      "responsible": "L9749",
      "servername": "sv00241"
    },
    {
      "applier": "G12866",
      "id": 242,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "G12866",
      "servername": "sv00242"
    },
    {
      "applier": "G12866",
      "id": 243,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "G12866",
      "servername": "sv00243"
    },
    {
      "applier": "G12866",
      "id": 244,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "G12866",
      "servername": "sv00244"
    },
    {
      "applier": "G12866",
      "id": 245,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "G12866",
      "servername": "sv00245"
    },
    {
      "applier": "D7982",
      "id": 246,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "W0889",
      "servername": "sv00246"
    },
    {
      "applier": "D7982",
      "id": 247,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "W0889",
      "servername": "sv00247"
    },
    {
      "applier": "D7982",
      "id": 248,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "W0889",
      "servername": "sv00248"
    },
    {
      "applier": "D7982",
      "id": 249,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "W0889",
      "servername": "sv00249"
    },
    {
      "applier": "D7982",
      "id": 250,
      "owner": "R1601",
      "purpose": "Isilon",
      "responsible": "D7982",
      "servername": "sv00250"
    },
    {
      "applier": "D7982",
      "id": 251,
      "owner": "R1601",
      "purpose": "Isilon",
      "responsible": "D7982",
      "servername": "sv00251"
    },
    {
      "applier": "D18547",
      "id": 252,
      "owner": "F1768",
      "purpose": "SQL Server W2k12R2",
      "responsible": "D18547",
      "servername": "sv00252"
    },
    {
      "applier": "C0371",
      "id": 253,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "C0371",
      "servername": "sv00253"
    },
    {
      "applier": "C0371",
      "id": 254,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "C0371",
      "servername": "sv00254"
    },
    {
      "applier": "A1912",
      "id": 255,
      "owner": "B11210",
      "purpose": "VM File server for Air Products",
      "responsible": "A1912",
      "servername": "sv00255"
    },
    {
      "applier": "A0423",
      "id": 256,
      "owner": "S0295",
      "purpose": "SNTC Collector Server",
      "responsible": "A0423",
      "servername": "sv00256"
    },
    {
      "applier": "A0423",
      "id": 257,
      "owner": "A0423",
      "purpose": "ESX Host Delfzijl",
      "responsible": "A0423",
      "servername": "sv00257"
    },
    {
      "applier": "L9749",
      "id": 258,
      "owner": "T0389",
      "purpose": "Schichtbuch Finito Server",
      "responsible": "L9749",
      "servername": "sv00258"
    },
    {
      "applier": "S0344",
      "id": 259,
      "owner": "M2474",
      "purpose": "Panagenda HUMAN",
      "responsible": "O1854",
      "servername": "sv00259"
    },
    {
      "applier": "S18344",
      "id": 260,
      "owner": "S18344",
      "purpose": "Datacenter Management System",
      "responsible": "S18344",
      "servername": "sv00260"
    },
    {
      "applier": "S18344",
      "id": 261,
      "owner": "S18344",
      "purpose": "Datacenter Management System",
      "responsible": "S18344",
      "servername": "sv00261"
    },
    {
      "applier": "S18344",
      "id": 262,
      "owner": "S18344",
      "purpose": "Datacenter Management System",
      "responsible": "S18344",
      "servername": "sv00262"
    },
    {
      "applier": "S18344",
      "id": 263,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00263"
    },
    {
      "applier": "S18344",
      "id": 264,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00264"
    },
    {
      "applier": "S18344",
      "id": 265,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00265"
    },
    {
      "applier": "S18344",
      "id": 266,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00266"
    },
    {
      "applier": "S18344",
      "id": 267,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00267"
    },
    {
      "applier": "S18344",
      "id": 268,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00268"
    },
    {
      "applier": "S18344",
      "id": 269,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00269"
    },
    {
      "applier": "S18344",
      "id": 270,
      "owner": "S0344",
      "purpose": "Citrix JumpHost ES1/ES2",
      "responsible": "S0344",
      "servername": "sv00270"
    },
    {
      "applier": "S18344",
      "id": 271,
      "owner": "S0344",
      "purpose": "Citrix JumpHost ES1/ES2",
      "responsible": "S0344",
      "servername": "sv00271"
    },
    {
      "applier": "S18344",
      "id": 272,
      "owner": "S0344",
      "purpose": "Citrix JumpHost ES1/ES2",
      "responsible": "S0344",
      "servername": "sv00272"
    },
    {
      "applier": "S18344",
      "id": 273,
      "owner": "S0344",
      "purpose": "Citrix JumpHost ES1/ES2",
      "responsible": "S0344",
      "servername": "sv00273"
    },
    {
      "applier": "S18344",
      "id": 274,
      "owner": "S0344",
      "purpose": "Citrix JumpHost ES1/ES2",
      "responsible": "S0344",
      "servername": "sv00274"
    },
    {
      "applier": "S18344",
      "id": 275,
      "owner": "S0344",
      "purpose": "Citrix JumpHost ES1/ES2",
      "responsible": "S0344",
      "servername": "sv00275"
    },
    {
      "applier": "S18344",
      "id": 276,
      "owner": "S0344",
      "purpose": "Citrix JumpHost ES1/ES2",
      "responsible": "S0344",
      "servername": "sv00276"
    },
    {
      "applier": "S18344",
      "id": 277,
      "owner": "S0344",
      "purpose": "Citrix JumpHost ES1/ES2",
      "responsible": "S0344",
      "servername": "sv00277"
    },
    {
      "applier": "S18344",
      "id": 278,
      "owner": "S0344",
      "purpose": "Citrix JumpHost ES1/ES2",
      "responsible": "S0344",
      "servername": "sv00278"
    },
    {
      "applier": "S18344",
      "id": 279,
      "owner": "S0344",
      "purpose": "Citrix JumpHost ES1/ES2",
      "responsible": "S0344",
      "servername": "sv00279"
    },
    {
      "applier": "S18344",
      "id": 280,
      "owner": "S0344",
      "purpose": "Citrix JumpHost ES1/ES2",
      "responsible": "S0344",
      "servername": "sv00280"
    },
    {
      "applier": "S18344",
      "id": 281,
      "owner": "S0344",
      "purpose": "Citrix JumpHost ES1/ES2",
      "responsible": "S0344",
      "servername": "sv00281"
    },
    {
      "applier": "S18344",
      "id": 282,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00282"
    },
    {
      "applier": "S18344",
      "id": 283,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00283"
    },
    {
      "applier": "S18344",
      "id": 284,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00284"
    },
    {
      "applier": "S18344",
      "id": 285,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00285"
    },
    {
      "applier": "S18344",
      "id": 286,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00286"
    },
    {
      "applier": "S18344",
      "id": 287,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00287"
    },
    {
      "applier": "S18344",
      "id": 288,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00288"
    },
    {
      "applier": "S18344",
      "id": 289,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00289"
    },
    {
      "applier": "S18344",
      "id": 290,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00290"
    },
    {
      "applier": "S18344",
      "id": 291,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00291"
    },
    {
      "applier": "S18344",
      "id": 292,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00292"
    },
    {
      "applier": "S18344",
      "id": 293,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00293"
    },
    {
      "applier": "S18344",
      "id": 294,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00294"
    },
    {
      "applier": "S18344",
      "id": 295,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00295"
    },
    {
      "applier": "S18344",
      "id": 296,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00296"
    },
    {
      "applier": "S18344",
      "id": 297,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00297"
    },
    {
      "applier": "S18344",
      "id": 298,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00298"
    },
    {
      "applier": "S18344",
      "id": 299,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00299"
    },
    {
      "applier": "S18344",
      "id": 300,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00300"
    },
    {
      "applier": "S18344",
      "id": 301,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00301"
    },
    {
      "applier": "S18344",
      "id": 302,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00302"
    },
    {
      "applier": "S18344",
      "id": 303,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00303"
    },
    {
      "applier": "S18344",
      "id": 304,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00304"
    },
    {
      "applier": "S18344",
      "id": 305,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00305"
    },
    {
      "applier": "S18344",
      "id": 306,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00306"
    },
    {
      "applier": "S18344",
      "id": 307,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00307"
    },
    {
      "applier": "S18344",
      "id": 308,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00308"
    },
    {
      "applier": "S18344",
      "id": 309,
      "owner": "S0344",
      "purpose": "Datacenter Management System",
      "responsible": "S0344",
      "servername": "sv00309"
    },
    {
      "applier": "D7982",
      "id": 310,
      "owner": "K0962",
      "purpose": "Applikation Server",
      "responsible": "D7982",
      "servername": "sv00310"
    },
    {
      "applier": "L9749",
      "id": 311,
      "owner": "D0907",
      "purpose": "EPO 5.x Development",
      "responsible": "L9749",
      "servername": "sv00311"
    },
    {
      "applier": "C0371",
      "id": 312,
      "owner": "R2146",
      "purpose": "PIMS Server TAR DOS",
      "responsible": "C0371",
      "servername": "sv00312"
    },
    {
      "applier": "C0371",
      "id": 313,
      "owner": "R2146",
      "purpose": "PIMS CIMIO DOS",
      "responsible": "C0371",
      "servername": "sv00313"
    },
    {
      "applier": "C0371",
      "id": 314,
      "owner": "R2146",
      "purpose": "PIMS CIMIO DOS",
      "responsible": "C0371",
      "servername": "sv00314"
    },
    {
      "applier": "S18344",
      "id": 315,
      "owner": "B6833",
      "purpose": "WWI/Experrtserver",
      "responsible": "S18344",
      "servername": "sv00315"
    },
    {
      "applier": "L9749",
      "id": 316,
      "owner": "M23734",
      "purpose": "ecmdevbrava",
      "responsible": "L9749",
      "servername": "sv00316"
    },
    {
      "applier": "L9749",
      "id": 317,
      "owner": "M23734",
      "purpose": "ecmqabrava",
      "responsible": "L9749",
      "servername": "sv00317"
    },
    {
      "applier": "L9749",
      "id": 318,
      "owner": "C1181",
      "purpose": "SAP HANA Cloud Connector",
      "responsible": "L9749",
      "servername": "sv00318"
    },
    {
      "applier": "L9749",
      "id": 319,
      "owner": "S13571",
      "purpose": "Veeam Proxy Server",
      "responsible": "L9749",
      "servername": "sv00319"
    },
    {
      "applier": "L9749",
      "id": 320,
      "owner": "S13571",
      "purpose": "Veeam Proxy Server",
      "responsible": "L9749",
      "servername": "sv00320"
    },
    {
      "applier": "L9749",
      "id": 321,
      "owner": "C11917",
      "purpose": "ArcSight Logger ",
      "responsible": "L9749",
      "servername": "sv00321"
    },
    {
      "applier": "L9749",
      "id": 322,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "L9749",
      "servername": "sv00322"
    },
    {
      "applier": "L9749",
      "id": 323,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "L9749",
      "servername": "sv00323"
    },
    {
      "applier": "L9749",
      "id": 324,
      "owner": "T8973",
      "purpose": "ASP Portal Webinterface",
      "responsible": "L9749",
      "servername": "sv00324"
    },
    {
      "applier": "L9749",
      "id": 325,
      "owner": "T0389",
      "purpose": "ASP Portal Webinterface",
      "responsible": "L9749",
      "servername": "sv00325"
    },
    {
      "applier": "L9749",
      "id": 326,
      "owner": "U0358",
      "purpose": "WFA Server",
      "responsible": "L9749",
      "servername": "sv00326"
    },
    {
      "applier": "L9749",
      "id": 327,
      "owner": "U0358",
      "purpose": "WFA Perfmon Server",
      "responsible": "L9749",
      "servername": "sv00327"
    },
    {
      "applier": "L9749",
      "id": 328,
      "owner": "U0358",
      "purpose": "WFA Jumphost Server",
      "responsible": "L9749",
      "servername": "sv00328"
    },
    {
      "applier": "L9749",
      "id": 329,
      "owner": "U0358",
      "purpose": "EMEA Snap Creator Framework",
      "responsible": "L9749",
      "servername": "sv00329"
    },
    {
      "applier": "L9749",
      "id": 330,
      "owner": "B1662",
      "purpose": "Admin.Net 2 QA Webserver",
      "responsible": "L9749",
      "servername": "sv00330"
    },
    {
      "applier": "L9749",
      "id": 331,
      "owner": "U0358",
      "purpose": "OCUM Appliance",
      "responsible": "L9749",
      "servername": "sv00331"
    },
    {
      "applier": "L9749",
      "id": 332,
      "owner": "U0358",
      "purpose": "EMEA Perfmon Appliance Netapp",
      "responsible": "L9749",
      "servername": "sv00332"
    },
    {
      "applier": "L9749",
      "id": 333,
      "owner": "T8973",
      "purpose": " ASP-Portal Webinterface",
      "responsible": "L9749",
      "servername": "sv00333"
    },
    {
      "applier": "L9749",
      "id": 334,
      "owner": "T8973",
      "purpose": "ASP-Portal Webinterface",
      "responsible": "L9749",
      "servername": "sv00334"
    },
    {
      "applier": "L9749",
      "id": 335,
      "owner": "F1768",
      "purpose": "SQL Shared Server",
      "responsible": "L9749",
      "servername": "sv00335"
    },
    {
      "applier": "h17255",
      "id": 336,
      "owner": "H17255",
      "purpose": "ESXi Host for Porduction IT",
      "responsible": "H17255",
      "servername": "sv00336"
    },
    {
      "applier": "h17255",
      "id": 337,
      "owner": "H17255",
      "purpose": "ESXi Host for Production IT",
      "responsible": "H17255",
      "servername": "sv00337"
    },
    {
      "applier": "S13571",
      "id": 338,
      "owner": "S13571",
      "purpose": "UCS Platform Emulator",
      "responsible": "S13571",
      "servername": "sv00338"
    },
    {
      "applier": "S18344",
      "id": 339,
      "owner": "B1662",
      "purpose": "CyberArk Test - PrimaryVault",
      "responsible": "S18344",
      "servername": "sv00339"
    },
    {
      "applier": "S18344",
      "id": 340,
      "owner": "B1662",
      "purpose": "CyberArk Test - DR Vault",
      "responsible": "S18344",
      "servername": "sv00340"
    },
    {
      "applier": "S18344",
      "id": 341,
      "owner": "B1662",
      "purpose": "CyberArk Test - CPM",
      "responsible": "S18344",
      "servername": "sv00341"
    },
    {
      "applier": "S18344",
      "id": 342,
      "owner": "B1662",
      "purpose": "CyberArk Test - PVWA",
      "responsible": "S18344",
      "servername": "sv00342"
    },
    {
      "applier": "K15717",
      "id": 343,
      "owner": "S19285",
      "purpose": "SFTP File Server",
      "responsible": "K15717",
      "servername": "sv00343"
    },
    {
      "applier": "K15717",
      "id": 344,
      "owner": "S19285",
      "purpose": "SFTP File Server",
      "responsible": "K15717",
      "servername": "sv00344"
    },
    {
      "applier": "D18547",
      "id": 345,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "L9749",
      "servername": "sv00345"
    },
    {
      "applier": "D18547",
      "id": 346,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "L9749",
      "servername": "sv00346"
    },
    {
      "applier": "D18547",
      "id": 347,
      "owner": "O1854",
      "purpose": "ASP Terminal Server",
      "responsible": "L9749",
      "servername": "sv00347"
    },
    {
      "applier": "L9749",
      "id": 348,
      "owner": "S13571",
      "purpose": "VEEAM Proxy Server",
      "responsible": "L9749",
      "servername": "sv00348"
    },
    {
      "applier": "L9749",
      "id": 349,
      "owner": "S13571",
      "purpose": "VEEAM Proxy Server",
      "responsible": "L9749",
      "servername": "sv00349"
    },
    {
      "applier": "L9749",
      "id": 350,
      "owner": "M23055",
      "purpose": "Betrieb LogPDS Produktiv",
      "responsible": "L9749",
      "servername": "sv00350"
    },
    {
      "applier": "L9749",
      "id": 351,
      "owner": "M23055",
      "purpose": "Betrieb LogPDS Test",
      "responsible": "L9749",
      "servername": "sv00351"
    },
    {
      "applier": "O0067",
      "id": 352,
      "owner": "B6833",
      "purpose": "ITSM AM-WEB3-PROD",
      "responsible": "O0067",
      "servername": "sv00352"
    },
    {
      "applier": "L9749",
      "id": 353,
      "owner": "D0106",
      "purpose": "TSM Manager FRA1",
      "responsible": "L9749",
      "servername": "sv00353"
    },
    {
      "applier": "K15717",
      "id": 354,
      "owner": "M23827",
      "purpose": "Aspen Process Controller, Dashboards",
      "responsible": "K15717",
      "servername": "sv00354"
    },
    {
      "applier": "A1912",
      "id": 355,
      "owner": "K12285",
      "purpose": "Server f\u00c3\u00bcr MIM CM Installation und User",
      "responsible": "A1912",
      "servername": "sv00355"
    },
    {
      "applier": "L9749",
      "id": 356,
      "owner": "A1019",
      "purpose": "BlackBerry 12 Server",
      "responsible": "L9749",
      "servername": "sv00356"
    },
    {
      "applier": "A1912",
      "id": 357,
      "owner": "A0423",
      "purpose": "ESX Host Delfzjil",
      "responsible": "A1912",
      "servername": "sv00357"
    },
    {
      "applier": "A1912",
      "id": 358,
      "owner": "A0423",
      "purpose": "ESX Host Delfzjil",
      "responsible": "A1912",
      "servername": "sv00358"
    },
    {
      "applier": "O0067",
      "id": 359,
      "owner": "A1019",
      "purpose": "Blackberry BES12 Server",
      "responsible": "O0067",
      "servername": "sv00359"
    },
    {
      "applier": "A1912",
      "id": 360,
      "owner": "B0163",
      "purpose": "Projekt  Evonik - HR Business Center PoC ",
      "responsible": "A1912",
      "servername": "sv00360"
    },
    {
      "applier": "A1912",
      "id": 361,
      "owner": "K12285",
      "purpose": "Server f\u00c3\u00bcr MIM CM Installation und User",
      "responsible": "A1912",
      "servername": "sv00361"
    },
    {
      "applier": "A1912",
      "id": 362,
      "owner": "K12285",
      "purpose": "Server f\u00c3\u00bcr MIM CM Installation und User",
      "responsible": "A1912",
      "servername": "sv00362"
    },
    {
      "applier": "A1912",
      "id": 363,
      "owner": "K12285",
      "purpose": "Server f\u00c3\u00bcr MIM CM Installation und User",
      "responsible": "A1912",
      "servername": "sv00363"
    },
    {
      "applier": "A1912",
      "id": 364,
      "owner": "O1854",
      "purpose": "VM Special ASP Terminal Server",
      "responsible": "A1912",
      "servername": "sv00364"
    },
    {
      "applier": "A1912",
      "id": 365,
      "owner": "O1854",
      "purpose": "VM Special ASP Terminal Server",
      "responsible": "A1912",
      "servername": "sv00365"
    },
    {
      "applier": "A1912",
      "id": 366,
      "owner": "O1854",
      "purpose": "VM Special ASP Terminal Server",
      "responsible": "A1912",
      "servername": "sv00366"
    },
    {
      "applier": "D15437",
      "id": 367,
      "owner": "F7897",
      "purpose": "DC degussa.com",
      "responsible": "D15437",
      "servername": "sv00367"
    },
    {
      "applier": "D15437",
      "id": 368,
      "owner": "F7897",
      "purpose": "DC americas.degussanet.com",
      "responsible": "D15437",
      "servername": "sv00368"
    },
    {
      "applier": "D15437",
      "id": 369,
      "owner": "F7897",
      "purpose": "DC asia.degussanet.com",
      "responsible": "D15437",
      "servername": "sv00369"
    },
    {
      "applier": "A1912",
      "id": 370,
      "owner": "A0423",
      "purpose": "ESX Host Essen Rellinghaus",
      "responsible": "A1912",
      "servername": "sv00370"
    },
    {
      "applier": "A1912",
      "id": 371,
      "owner": "A0423",
      "purpose": "ESX Host Essen Rellinghaus",
      "responsible": "A1912",
      "servername": "sv00371"
    },
    {
      "applier": "A1912",
      "id": 372,
      "owner": "A0423",
      "purpose": "ESX Host Essen Rellinghaus",
      "responsible": "A1912",
      "servername": "sv00372"
    },
    {
      "applier": "A1912",
      "id": 373,
      "owner": "A0423",
      "purpose": "ESX Host Essen Rellinghaus",
      "responsible": "A1912",
      "servername": "sv00373"
    },
    {
      "applier": "S18344",
      "id": 374,
      "owner": "B1662",
      "purpose": "CyberArk Prod - Primary Vault",
      "responsible": "S18344",
      "servername": "sv00374"
    },
    {
      "applier": "S18344",
      "id": 375,
      "owner": "B1662",
      "purpose": "CyberArk Prod - DR Vault",
      "responsible": "S18344",
      "servername": "sv00375"
    },
    {
      "applier": "S18344",
      "id": 376,
      "owner": "B1662",
      "purpose": "CyberArk Prod - CPM",
      "responsible": "S18344",
      "servername": "sv00376"
    },
    {
      "applier": "S18344",
      "id": 377,
      "owner": "B1662",
      "purpose": "CyberArk Prod - PVWA 01",
      "responsible": "S18344",
      "servername": "sv00377"
    },
    {
      "applier": "S18344",
      "id": 378,
      "owner": "B1662",
      "purpose": "CyberArk Prod - PVWA 02",
      "responsible": "S18344",
      "servername": "sv00378"
    },
    {
      "applier": "d1332",
      "id": 379,
      "owner": "D1332",
      "purpose": "ANTI-SPAM-Software",
      "responsible": "D1332",
      "servername": "sv00379"
    },
    {
      "applier": "d1332",
      "id": 380,
      "owner": "D1332",
      "purpose": "ANTI-SPAM-Software",
      "responsible": "D1332",
      "servername": "sv00380"
    },
    {
      "applier": "S0344",
      "id": 381,
      "owner": "S0344",
      "purpose": "HPSUM",
      "responsible": "S0344",
      "servername": "sv00381"
    },
    {
      "applier": "S19749",
      "id": 382,
      "owner": "S19749",
      "purpose": "ASP Terminal Server",
      "responsible": "S19749",
      "servername": "sv00382"
    },
    {
      "applier": "S19749",
      "id": 383,
      "owner": "S19749",
      "purpose": "citrix server",
      "responsible": "S19749",
      "servername": "sv00383"
    },
    {
      "applier": "B13085",
      "id": 384,
      "owner": "M23816",
      "purpose": "SP-0500 NOM",
      "responsible": "B13085",
      "servername": "sv00384"
    },
    {
      "applier": "B13085",
      "id": 385,
      "owner": "M23816",
      "purpose": "SP-0500 NOM",
      "responsible": "B13085",
      "servername": "sv00385"
    },
    {
      "applier": "B13085",
      "id": 386,
      "owner": "M23816",
      "purpose": "SP-0500 NOM",
      "responsible": "B13085",
      "servername": "sv00386"
    },
    {
      "applier": "B13085",
      "id": 387,
      "owner": "M23816",
      "purpose": "SP-0500 NOM",
      "responsible": "B13085",
      "servername": "sv00387"
    },
    {
      "applier": "B13085",
      "id": 388,
      "owner": "F1768",
      "purpose": "SQL Server for SP-0500 NOM",
      "responsible": "B13085",
      "servername": "sv00388"
    },
    {
      "applier": "D15437",
      "id": 389,
      "owner": "S19285",
      "purpose": "Oracle Server (strictly confidential)",
      "responsible": "D15437",
      "servername": "sv00389"
    },
    {
      "applier": "D15437",
      "id": 390,
      "owner": "F7897",
      "purpose": "DC eu.degussanet.com",
      "responsible": "D15437",
      "servername": "sv00390"
    },
    {
      "applier": "D15437",
      "id": 391,
      "owner": "F7897",
      "purpose": "DC eu.degussanet.com",
      "responsible": "D15437",
      "servername": "sv00391"
    },
    {
      "applier": "D15437",
      "id": 392,
      "owner": "F7897",
      "purpose": "DC eu.degussanet.com",
      "responsible": "D15437",
      "servername": "sv00392"
    },
    {
      "applier": "D15437",
      "id": 393,
      "owner": "F7897",
      "purpose": "DC ead.dom",
      "responsible": "D15437",
      "servername": "sv00393"
    },
    {
      "applier": "S0344",
      "id": 394,
      "owner": "S0344",
      "purpose": "VMware Log Insight",
      "responsible": "S0344",
      "servername": "sv00394"
    },
    {
      "applier": "S13571",
      "id": 395,
      "owner": "S13571",
      "purpose": "Veeam Gateway ES1",
      "responsible": "S13571",
      "servername": "sv00395"
    },
    {
      "applier": "S13571",
      "id": 396,
      "owner": "S13571",
      "purpose": "Veeam Gateway ES1",
      "responsible": "S13571",
      "servername": "sv00396"
    },
    {
      "applier": "S13571",
      "id": 397,
      "owner": "S13571",
      "purpose": "Veeam Gateway ES1",
      "responsible": "S13571",
      "servername": "sv00397"
    },
    {
      "applier": "S13571",
      "id": 398,
      "owner": "S13571",
      "purpose": "Veeam Gateway ES2",
      "responsible": "S13571",
      "servername": "sv00398"
    },
    {
      "applier": "S13571",
      "id": 399,
      "owner": "S13571",
      "purpose": "Veeam Gateway ES2",
      "responsible": "S13571",
      "servername": "sv00399"
    },
    {
      "applier": "S13571",
      "id": 400,
      "owner": "S13571",
      "purpose": "Veeam Gateway ES2",
      "responsible": "S13571",
      "servername": "sv00400"
    },
    {
      "applier": "D18268",
      "id": 401,
      "owner": "A0905",
      "purpose": "PLS data transfer server",
      "responsible": "D18268",
      "servername": "sv00401"
    },
    {
      "applier": "D18268",
      "id": 402,
      "owner": "M3956",
      "purpose": "Honeypot Manager",
      "responsible": "D18268",
      "servername": "sv00402"
    },
    {
      "applier": "D18268",
      "id": 403,
      "owner": "J9877",
      "purpose": "EWM system",
      "responsible": "D18268",
      "servername": "sv00403"
    },
    {
      "applier": "S0344",
      "id": 404,
      "owner": "E9905",
      "purpose": "Scripting Server IT-UP Prod1",
      "responsible": "S0344",
      "servername": "sv00404"
    },
    {
      "applier": "S0344",
      "id": 405,
      "owner": "E9905",
      "purpose": "Scripting Server IT-UP Prod2",
      "responsible": "S0344",
      "servername": "sv00405"
    },
    {
      "applier": "S0344",
      "id": 406,
      "owner": "E9905",
      "purpose": "Scripting Server IT-UP QA",
      "responsible": "S0344",
      "servername": "sv00406"
    },
    {
      "applier": "O0067",
      "id": 407,
      "owner": "S13571",
      "purpose": "Veeam Proxy Server",
      "responsible": "O0067",
      "servername": "sv00407"
    },
    {
      "applier": "O0067",
      "id": 408,
      "owner": "S13571",
      "purpose": "Veeam Proxy Server",
      "responsible": "O0067",
      "servername": "sv00408"
    },
    {
      "applier": "O0067",
      "id": 409,
      "owner": "S13571",
      "purpose": "Veeam Proxy Server",
      "responsible": "O0067",
      "servername": "sv00409"
    },
    {
      "applier": "O0067",
      "id": 410,
      "owner": "S13571",
      "purpose": "Veeam Proxy Server",
      "responsible": "O0067",
      "servername": "sv00410"
    },
    {
      "applier": "O0067",
      "id": 411,
      "owner": "S13571",
      "purpose": "Veeam Proxy Server",
      "responsible": "O0067",
      "servername": "sv00411"
    },
    {
      "applier": "O0067",
      "id": 412,
      "owner": "S13571",
      "purpose": "Veeam Proxy Server",
      "responsible": "O0067",
      "servername": "sv00412"
    },
    {
      "applier": "O0067",
      "id": 413,
      "owner": "M23816",
      "purpose": "Sharepoint SP-0500 NOM",
      "responsible": "O0067",
      "servername": "sv00413"
    },
    {
      "applier": "O0067",
      "id": 414,
      "owner": "M23816",
      "purpose": "Sharepoint SP-0500 NOM",
      "responsible": "O0067",
      "servername": "sv00414"
    },
    {
      "applier": "O0067",
      "id": 415,
      "owner": "M23816",
      "purpose": "Sharepoint SP-0500 NOM",
      "responsible": "O0067",
      "servername": "sv00415"
    },
    {
      "applier": "O0067",
      "id": 416,
      "owner": "M23816",
      "purpose": "s",
      "responsible": "O0067",
      "servername": "sv00416"
    },
    {
      "applier": "O0067",
      "id": 417,
      "owner": "M0495",
      "purpose": "Domain Controller",
      "responsible": "O0067",
      "servername": "sv00417"
    },
    {
      "applier": "O0067",
      "id": 418,
      "owner": "M0495",
      "purpose": "Domain Controller",
      "responsible": "O0067",
      "servername": "sv00418"
    },
    {
      "applier": "O0067",
      "id": 419,
      "owner": "M0495",
      "purpose": "Domain Controller",
      "responsible": "O0067",
      "servername": "sv00419"
    },
    {
      "applier": "O0067",
      "id": 420,
      "owner": "M0495",
      "purpose": "Domain Controller",
      "responsible": "O0067",
      "servername": "sv00420"
    },
    {
      "applier": "O0067",
      "id": 421,
      "owner": "M0495",
      "purpose": "Domain Controller",
      "responsible": "O0067",
      "servername": "sv00421"
    },
    {
      "applier": "O0067",
      "id": 422,
      "owner": "M0495",
      "purpose": "Domain Controller",
      "responsible": "O0067",
      "servername": "sv00422"
    },
    {
      "applier": "O0067",
      "id": 423,
      "owner": "M0495",
      "purpose": "Domain Controller",
      "responsible": "O0067",
      "servername": "sv00423"
    },
    {
      "applier": "O0067",
      "id": 424,
      "owner": "M23816",
      "purpose": "Sharepoint SP-0000 DocAve",
      "responsible": "O0067",
      "servername": "sv00424"
    },
    {
      "applier": "S0344",
      "id": 425,
      "owner": "D1332",
      "purpose": "Ironport Reporting Server",
      "responsible": "S0344",
      "servername": "sv00425"
    },
    {
      "applier": "S18344",
      "id": 426,
      "owner": "G0436",
      "purpose": "Openscape Sofgate Wolfgang",
      "responsible": "S18344",
      "servername": "sv00426"
    },
    {
      "applier": "S18344",
      "id": 427,
      "owner": "G0436",
      "purpose": "Openscape Sofgate Wolfgang",
      "responsible": "S18344",
      "servername": "sv00427"
    },
    {
      "applier": "C0371",
      "id": 428,
      "owner": "K12285",
      "purpose": "SCEP Service",
      "responsible": "C0371",
      "servername": "sv00428"
    },
    {
      "applier": "D18268",
      "id": 429,
      "owner": "S20376",
      "purpose": "WAS-5100 -ELO",
      "responsible": "D18268",
      "servername": "sv00429"
    },
    {
      "applier": "A0423",
      "id": 430,
      "owner": "S20376",
      "purpose": "DEV Application Server",
      "responsible": "A0423",
      "servername": "sv00430"
    },
    {
      "applier": "D15437",
      "id": 431,
      "owner": "S13571",
      "purpose": "Veeam Proxy ES1",
      "responsible": "D15437",
      "servername": "sv00431"
    },
    {
      "applier": "D15437",
      "id": 432,
      "owner": "S13571",
      "purpose": "Veeam Proxy ES2 ",
      "responsible": "D15437",
      "servername": "sv00432"
    },
    {
      "applier": "A0423",
      "id": 433,
      "owner": "A0423",
      "purpose": "VDP Backup Server Antwerpen",
      "responsible": "A0423",
      "servername": "sv00433"
    },
    {
      "applier": "A0423",
      "id": 434,
      "owner": "A0423",
      "purpose": "VDP Backup Server Antwerpen",
      "responsible": "A0423",
      "servername": "sv00434"
    },
    {
      "applier": "A0423",
      "id": 435,
      "owner": "A0423",
      "purpose": "VDP Backup Server Marl",
      "responsible": "A0423",
      "servername": "sv00435"
    },
    {
      "applier": "A0423",
      "id": 436,
      "owner": "A0423",
      "purpose": "VDP Backup Server Marl",
      "responsible": "A0423",
      "servername": "sv00436"
    },
    {
      "applier": "C0371",
      "id": 437,
      "owner": "S13571",
      "purpose": "Veeam Proxy Server ",
      "responsible": "C0371",
      "servername": "sv00437"
    },
    {
      "applier": "C0371",
      "id": 438,
      "owner": "S13571",
      "purpose": "RFT00266643",
      "responsible": "C0371",
      "servername": "sv00438"
    },
    {
      "applier": "D18268",
      "id": 439,
      "owner": "M23816",
      "purpose": "SP-0500 NOM",
      "responsible": "D18268",
      "servername": "sv00439"
    },
    {
      "applier": "S19285",
      "id": 440,
      "owner": "S19285",
      "purpose": "Webserver for research project KeaP",
      "responsible": "S19285",
      "servername": "sv00440"
    },
    {
      "applier": "C10477",
      "id": 441,
      "owner": "J15936",
      "purpose": "MMA - NIR",
      "responsible": "C10477",
      "servername": "sv00441"
    },
    {
      "applier": "C10477",
      "id": 442,
      "owner": "J15936",
      "purpose": "MMA - NIR",
      "responsible": "C10477",
      "servername": "sv00442"
    },
    {
      "applier": "C10477",
      "id": 443,
      "owner": "J15936",
      "purpose": "MMA - NIR #3",
      "responsible": "C10477",
      "servername": "sv00443"
    },
    {
      "applier": "C10477",
      "id": 444,
      "owner": "J15936",
      "purpose": "MMA - NIR #4",
      "responsible": "C10477",
      "servername": "sv00444"
    },
    {
      "applier": "D15437",
      "id": 446,
      "owner": "D0106",
      "purpose": "Operation Center",
      "responsible": "D15437",
      "servername": "sv00446"
    },
    {
      "applier": "S0344",
      "id": 447,
      "owner": "S13571",
      "purpose": "GXP Veeam Gateway (ES1CLU01)",
      "responsible": "S0344",
      "servername": "sv00447"
    },
    {
      "applier": "S0344",
      "id": 448,
      "owner": "S13571",
      "purpose": "GXP Veeam Gateway (ES1HANACLU01)",
      "responsible": "S0344",
      "servername": "sv00448"
    },
    {
      "applier": "S0344",
      "id": 449,
      "owner": "S13571",
      "purpose": "GXP Veeam Gateway (ES1HC01CLU01)",
      "responsible": "S0344",
      "servername": "sv00449"
    },
    {
      "applier": "S0344",
      "id": 450,
      "owner": "S13571",
      "purpose": "GXP Veeam Gateway (ES1ORACLU01)",
      "responsible": "S0344",
      "servername": "sv00450"
    },
    {
      "applier": "S0344",
      "id": 451,
      "owner": "S13571",
      "purpose": "GXP Veeam Gateway (ES2CLU01)",
      "responsible": "S0344",
      "servername": "sv00451"
    },
    {
      "applier": "S0344",
      "id": 452,
      "owner": "S13571",
      "purpose": "GXP Veeam Gateway (ES2HANACLU01)",
      "responsible": "S0344",
      "servername": "sv00452"
    },
    {
      "applier": "S0344",
      "id": 453,
      "owner": "S13571",
      "purpose": "GXP Veeam Gateway (ES2HC01CLU01)",
      "responsible": "S0344",
      "servername": "sv00453"
    },
    {
      "applier": "S0344",
      "id": 454,
      "owner": "S13571",
      "purpose": "GXP Veeam Gateway (ES2SQLCLU01)",
      "responsible": "S0344",
      "servername": "sv00454"
    },
    {
      "applier": "S0344",
      "id": 455,
      "owner": "S13571",
      "purpose": "GXP Veeam Proxy (ES1CLU01)",
      "responsible": "S0344",
      "servername": "sv00455"
    },
    {
      "applier": "S0344",
      "id": 456,
      "owner": "S13571",
      "purpose": "GXP Veeam Proxy (ES1HANACLU01)",
      "responsible": "S0344",
      "servername": "sv00456"
    },
    {
      "applier": "S0344",
      "id": 457,
      "owner": "S13571",
      "purpose": "GXP Veeam Proxy (ES1HC01CLU01)",
      "responsible": "S0344",
      "servername": "sv00457"
    },
    {
      "applier": "S0344",
      "id": 458,
      "owner": "S13571",
      "purpose": "GXP Veeam Proxy (ES1ORACLU01)",
      "responsible": "S0344",
      "servername": "sv00458"
    },
    {
      "applier": "S0344",
      "id": 459,
      "owner": "S13571",
      "purpose": "GXP Veeam Proxy (ES2CLU01)",
      "responsible": "S0344",
      "servername": "sv00459"
    },
    {
      "applier": "S0344",
      "id": 460,
      "owner": "S13571",
      "purpose": "GXP Veeam Proxy (ES2HANACLU01)",
      "responsible": "S0344",
      "servername": "sv00460"
    },
    {
      "applier": "S0344",
      "id": 461,
      "owner": "S13571",
      "purpose": "GXP Veeam Proxy (ES2HC01CLU01)",
      "responsible": "S0344",
      "servername": "sv00461"
    },
    {
      "applier": "S0344",
      "id": 462,
      "owner": "S13571",
      "purpose": "GXP Veeam Proxy (ES2SQLCLU01)",
      "responsible": "S0344",
      "servername": "sv00462"
    },
    {
      "applier": "D18268",
      "id": 463,
      "owner": "M23816",
      "purpose": "SP-0500 NOM",
      "responsible": "D18268",
      "servername": "sv00463"
    },
    {
      "applier": "D15437",
      "id": 464,
      "owner": "F1768",
      "purpose": "PAS-X Application Server",
      "responsible": "D15437",
      "servername": "sv00464"
    },
    {
      "applier": "D15437",
      "id": 465,
      "owner": "F1768",
      "purpose": "PAS-X Background Process Server",
      "responsible": "D15437",
      "servername": "sv00465"
    },
    {
      "applier": "A0423",
      "id": 466,
      "owner": "G0806",
      "purpose": "Softgate Server Essen",
      "responsible": "A0423",
      "servername": "sv00466"
    },
    {
      "applier": "A0423",
      "id": 467,
      "owner": "G0806",
      "purpose": "Softgate Server Essen",
      "responsible": "A0423",
      "servername": "sv00467"
    },
    {
      "applier": "A0423",
      "id": 468,
      "owner": "G0806",
      "purpose": "Softgate Server Essen",
      "responsible": "A0423",
      "servername": "sv00468"
    },
    {
      "applier": "A0423",
      "id": 469,
      "owner": "G0806",
      "purpose": "Softgate Server Essen",
      "responsible": "A0423",
      "servername": "sv00469"
    },
    {
      "applier": "S18344",
      "id": 470,
      "owner": "F0327",
      "purpose": "EPOS Windowsprintserver for Shanghai",
      "responsible": "F0327",
      "servername": "sv00470"
    },
    {
      "applier": "S0344",
      "id": 471,
      "owner": "S0344",
      "purpose": "vRealize Operations Manager Appliance",
      "responsible": "S0344",
      "servername": "sv00471"
    },
    {
      "applier": "S0344",
      "id": 472,
      "owner": "S0344",
      "purpose": "vRealize Infrastructure Navigator",
      "responsible": "S0344",
      "servername": "sv00472"
    },
    {
      "applier": "A0423",
      "id": 473,
      "owner": "M34002",
      "purpose": "SQL Server",
      "responsible": "A0423",
      "servername": "sv00473"
    },
    {
      "applier": "S0344",
      "id": 474,
      "owner": "S0344",
      "purpose": "Cisco UCS Performance Manager",
      "responsible": "S0344",
      "servername": "sv00474"
    },
    {
      "applier": "C0371",
      "id": 475,
      "owner": "M23816",
      "purpose": "SP-0300 Enterprise Search",
      "responsible": "C0371",
      "servername": "sv00475"
    },
    {
      "applier": "C0371",
      "id": 476,
      "owner": "M23816",
      "purpose": "SP-0300 Enterprise Search",
      "responsible": "C0371",
      "servername": "sv00476"
    },
    {
      "applier": "D18268",
      "id": 477,
      "owner": "J9877",
      "purpose": "EWM System",
      "responsible": "D18268",
      "servername": "sv00477"
    },
    {
      "applier": "C10477",
      "id": 478,
      "owner": "J15936",
      "purpose": "WES MMA NIR ESX Host",
      "responsible": "C10477",
      "servername": "sv00478"
    },
    {
      "applier": "T15463",
      "id": 479,
      "owner": "W11083",
      "purpose": "PMD Greenwich Aspen IP21",
      "responsible": "T15463",
      "servername": "sv00479"
    },
    {
      "applier": "T15463",
      "id": 480,
      "owner": "W11083",
      "purpose": "PMD Central Europe Aspen IP21",
      "responsible": "T15463",
      "servername": "sv00480"
    },
    {
      "applier": "G12866",
      "id": 481,
      "owner": "M23816",
      "purpose": "SP-0400 SharePoint Shared",
      "responsible": "G12866",
      "servername": "sv00481"
    },
    {
      "applier": "S0344",
      "id": 482,
      "owner": "T8973",
      "purpose": "ASP Terminal Server",
      "responsible": "S0344",
      "servername": "sv00482"
    },
    {
      "applier": "S0344",
      "id": 483,
      "owner": "T8973",
      "purpose": "ASP Terminal Server",
      "responsible": "S0344",
      "servername": "sv00483"
    },
    {
      "applier": "S0344",
      "id": 484,
      "owner": "T8973",
      "purpose": "ASP Terminal Server",
      "responsible": "S0344",
      "servername": "sv00484"
    },
    {
      "applier": "S0344",
      "id": 485,
      "owner": "T8973",
      "purpose": "ASP Terminal Server",
      "responsible": "S0344",
      "servername": "sv00485"
    },
    {
      "applier": "T15463",
      "id": 486,
      "owner": "D15437",
      "purpose": "Virtual fileserver for the eagle project",
      "responsible": "T15463",
      "servername": "sv00486"
    },
    {
      "applier": "T15463",
      "id": 487,
      "owner": "D15437",
      "purpose": "\tVirtual fileserver for the eagle project",
      "responsible": "T15463",
      "servername": "sv00487"
    },
    {
      "applier": "D18268",
      "id": 488,
      "owner": "F0327",
      "purpose": "EPOS Print Server",
      "responsible": "D18268",
      "servername": "sv00488"
    },
    {
      "applier": "T15463",
      "id": 489,
      "owner": "T12402",
      "purpose": "Infrastructure SCCM 2012",
      "responsible": "T15463",
      "servername": "sv00489"
    },
    {
      "applier": "T15463",
      "id": 490,
      "owner": "T12402",
      "purpose": "Infrastructure SCCM 2012",
      "responsible": "T15463",
      "servername": "sv00490"
    },
    {
      "applier": "H16862",
      "id": 491,
      "owner": "H16862",
      "purpose": "File Server",
      "responsible": "H16862",
      "servername": "sv00491"
    },
    {
      "applier": "D18268",
      "id": 492,
      "owner": "F0327",
      "purpose": "EPOS Print Server ",
      "responsible": "D18268",
      "servername": "sv00492"
    },
    {
      "applier": "D18268",
      "id": 493,
      "owner": "F0327",
      "purpose": "EPOS Print Server",
      "responsible": "D18268",
      "servername": "sv00493"
    },
    {
      "applier": "D18268",
      "id": 494,
      "owner": "I4738",
      "purpose": "Medox Server",
      "responsible": "D18268",
      "servername": "sv00494"
    },
    {
      "applier": "D18268",
      "id": 495,
      "owner": "I4738",
      "purpose": "Medox Server",
      "responsible": "D18268",
      "servername": "sv00495"
    },
    {
      "applier": "A0423",
      "id": 496,
      "owner": "G0806",
      "purpose": "Openscape Voice 4000 Softgate Server",
      "responsible": "A0423",
      "servername": "sv00496"
    },
    {
      "applier": "A0423",
      "id": 497,
      "owner": "G0806",
      "purpose": "Openscape Voice 4000 Softgate Server",
      "responsible": "A0423",
      "servername": "sv00497"
    },
    {
      "applier": "A0423",
      "id": 498,
      "owner": "O1854",
      "purpose": "APP ASP-Server Antwerpen",
      "responsible": "A0423",
      "servername": "sv00498"
    },
    {
      "applier": "A0423",
      "id": 499,
      "owner": "O1854",
      "purpose": "APP ASP-Server Antwerpen",
      "responsible": "A0423",
      "servername": "sv00499"
    },
    {
      "applier": "T15463",
      "id": 500,
      "owner": "S20376",
      "purpose": "Application Metasonic QA",
      "responsible": "S20376",
      "servername": "sv00500"
    },
    {
      "applier": "T15463",
      "id": 501,
      "owner": "S20376",
      "purpose": "Application Metasonic Prod",
      "responsible": "S20376",
      "servername": "sv00501"
    },
    {
      "applier": "T15463",
      "id": 502,
      "owner": "S19285",
      "purpose": "Key Management Software",
      "responsible": "S19285",
      "servername": "sv00502"
    },
    {
      "applier": "F0327",
      "id": 503,
      "owner": "F0327",
      "purpose": "EPOS Windowsprintserver",
      "responsible": "F0327",
      "servername": "sv00503"
    },
    {
      "applier": "F7813",
      "id": 504,
      "owner": "F7813",
      "purpose": "CASB - Skyhigh",
      "responsible": "F7813",
      "servername": "sv00504"
    },
    {
      "applier": "M23055",
      "id": 505,
      "owner": "M23055",
      "purpose": "Application server",
      "responsible": "M23055",
      "servername": "sv00505"
    },
    {
      "applier": "T15463",
      "id": 506,
      "owner": "S20903",
      "purpose": "WAS-5100-ELO-QA-Basisserver",
      "responsible": "A0423",
      "servername": "sv00506"
    },
    {
      "applier": "T15463",
      "id": 507,
      "owner": "S20903",
      "purpose": "WAS-5100-ELO-QA-Searchserver",
      "responsible": "A0423",
      "servername": "sv00507"
    },
    {
      "applier": "T15463",
      "id": 508,
      "owner": "S20903",
      "purpose": "WAS-5100-ELO-PROD-BasisServer",
      "responsible": "A0423",
      "servername": "sv00508"
    },
    {
      "applier": "T15463",
      "id": 509,
      "owner": "S20903",
      "purpose": "WAS-5100-ELO-PROD-SearchServer",
      "responsible": "A0423",
      "servername": "sv00509"
    },
    {
      "applier": "S18344",
      "id": 510,
      "owner": "M23055",
      "purpose": "Application Server HBC (office)",
      "responsible": "S18344",
      "servername": "sv00510"
    },
    {
      "applier": "S18344",
      "id": 511,
      "owner": "M23055",
      "purpose": "Application Server HBC (office)",
      "responsible": "S18344",
      "servername": "sv00511"
    },
    {
      "applier": "S18344",
      "id": 512,
      "owner": "M23055",
      "purpose": "Application Server HBC (web-dmz)",
      "responsible": "S18344",
      "servername": "sv00512"
    },
    {
      "applier": "A0423",
      "id": 513,
      "owner": "F7813",
      "purpose": "OVF Appliance CASP",
      "responsible": "A0423",
      "servername": "sv00513"
    },
    {
      "applier": "A0423",
      "id": 514,
      "owner": "F7813",
      "purpose": "OVF Appliance CASP",
      "responsible": "A0423",
      "servername": "sv00514"
    },
    {
      "applier": "D15437",
      "id": 515,
      "owner": "O1854",
      "purpose": "ASP eDesk-Core Server",
      "responsible": "D15437",
      "servername": "sv00515"
    },
    {
      "applier": "D15437",
      "id": 516,
      "owner": "O1854",
      "purpose": "ASP eDesk-Core Server",
      "responsible": "D15437",
      "servername": "sv00516"
    },
    {
      "applier": "D18268",
      "id": 517,
      "owner": "B6833",
      "purpose": "HP-ALM-DEV",
      "responsible": "D18268",
      "servername": "sv00517"
    },
    {
      "applier": "D18268",
      "id": 518,
      "owner": "W11083",
      "purpose": "PMD - Greenwich",
      "responsible": "D18268",
      "servername": "sv00518"
    },
    {
      "applier": "D18268",
      "id": 519,
      "owner": "B6833",
      "purpose": "Tomcat New Shared Cluster QA",
      "responsible": "D18268",
      "servername": "sv00519"
    },
    {
      "applier": "D18268",
      "id": 520,
      "owner": "B6833",
      "purpose": "Tomcat New Shared Cluster QA - 2",
      "responsible": "D18268",
      "servername": "sv00520"
    },
    {
      "applier": "D18268",
      "id": 521,
      "owner": "B6833",
      "purpose": "Tomcat New Shared Cluster QA - 3",
      "responsible": "D18268",
      "servername": "sv00521"
    },
    {
      "applier": "D18268",
      "id": 522,
      "owner": "B6833",
      "purpose": "Tomcat New Shared Cluster QA - 4",
      "responsible": "D18268",
      "servername": "sv00522"
    },
    {
      "applier": "C10477",
      "id": 523,
      "owner": "M39886",
      "purpose": "Sodium - LABSRV",
      "responsible": "C10477",
      "servername": "sv00523"
    },
    {
      "applier": "C10477",
      "id": 524,
      "owner": "M39886",
      "purpose": "Sodium - CASSRV2",
      "responsible": "C10477",
      "servername": "sv00524"
    },
    {
      "applier": "C10477",
      "id": 525,
      "owner": "M39886",
      "purpose": "Sodium - Intra",
      "responsible": "C10477",
      "servername": "sv00525"
    },
    {
      "applier": "C10477",
      "id": 526,
      "owner": "M39886",
      "purpose": "Sodium - DIBAC",
      "responsible": "C10477",
      "servername": "sv00526"
    },
    {
      "applier": "C10477",
      "id": 527,
      "owner": "M39886",
      "purpose": "Sodium - FinSRV",
      "responsible": "C10477",
      "servername": "sv00527"
    },
    {
      "applier": "C10477",
      "id": 528,
      "owner": "M39886",
      "purpose": "Sodium - SQLSRV1",
      "responsible": "C10477",
      "servername": "sv00528"
    },
    {
      "applier": "M39546",
      "id": 529,
      "owner": "A1019",
      "purpose": "Mobile Devices Management Server BES12",
      "responsible": "M39546",
      "servername": "sv00529"
    },
    {
      "applier": "T15463",
      "id": 530,
      "owner": "D0907",
      "purpose": "ePO Agent Handler in DMZ",
      "responsible": "D0907",
      "servername": "sv00530"
    },
    {
      "applier": "T15463",
      "id": 531,
      "owner": "M3180",
      "purpose": "File Server in VO-Krefeld area",
      "responsible": "M3180",
      "servername": "sv00531"
    },
    {
      "applier": "D18268",
      "id": 532,
      "owner": "M23734",
      "purpose": "Brava, Blazon and Rendition software",
      "responsible": "D18268",
      "servername": "sv00532"
    },
    {
      "applier": "O1854",
      "id": 533,
      "owner": "O1854",
      "purpose": "ASP Terminalserver",
      "responsible": "O1854",
      "servername": "sv00533"
    },
    {
      "applier": "O1854",
      "id": 534,
      "owner": "O1854",
      "purpose": "ASP Terminalserver",
      "responsible": "O1854",
      "servername": "sv00534"
    },
    {
      "applier": "O1854",
      "id": 535,
      "owner": "O1854",
      "purpose": "ASP Terminalserver",
      "responsible": "O1854",
      "servername": "sv00535"
    },
    {
      "applier": "O1854",
      "id": 536,
      "owner": "O1854",
      "purpose": "ASP Terminalserver",
      "responsible": "O1854",
      "servername": "sv00536"
    },
    {
      "applier": "O1854",
      "id": 537,
      "owner": "O1854",
      "purpose": "ASP Terminalserver",
      "responsible": "O1854",
      "servername": "sv00537"
    },
    {
      "applier": "O1854",
      "id": 538,
      "owner": "O1854",
      "purpose": "ASP Terminalserver",
      "responsible": "O1854",
      "servername": "sv00538"
    },
    {
      "applier": "O1854",
      "id": 539,
      "owner": "O1854",
      "purpose": "ASP Terminalserver",
      "responsible": "O1854",
      "servername": "sv00539"
    },
    {
      "applier": "O1854",
      "id": 540,
      "owner": "O1854",
      "purpose": "ASP Terminalserver",
      "responsible": "O1854",
      "servername": "sv00540"
    },
    {
      "applier": "S0344",
      "id": 541,
      "owner": "S0344",
      "purpose": "Brocade Network Advisor ES1",
      "responsible": "S0344",
      "servername": "sv00541"
    },
    {
      "applier": "S0344",
      "id": 542,
      "owner": "S0344",
      "purpose": "Brocade Network Advisor ES2",
      "responsible": "S0344",
      "servername": "sv00542"
    },
    {
      "applier": "T15463",
      "id": 543,
      "owner": "F8735",
      "purpose": "FileShare server",
      "responsible": "D15437",
      "servername": "sv00543"
    },
    {
      "applier": "T15463",
      "id": 544,
      "owner": "A22074",
      "purpose": "SP-0500 NOM",
      "responsible": "A22074",
      "servername": "sv00544"
    },
    {
      "applier": "T15463",
      "id": 545,
      "owner": "A22074",
      "purpose": "SP-0500 NOM",
      "responsible": "A22074",
      "servername": "sv00545"
    },
    {
      "applier": "D18268",
      "id": 546,
      "owner": "G0179",
      "purpose": "PST-Export",
      "responsible": "D18268",
      "servername": "sv00546"
    },
    {
      "applier": "D18268",
      "id": 547,
      "owner": "M23055",
      "purpose": "Smallworld GIS",
      "responsible": "D18268",
      "servername": "sv00547"
    },
    {
      "applier": "H1863",
      "id": 548,
      "owner": "H1863",
      "purpose": "New Installationfor DFS-R replication source",
      "responsible": "H1863",
      "servername": "sv00548"
    },
    {
      "applier": "S18344",
      "id": 549,
      "owner": "B1662",
      "purpose": "CyberArk Prod - Primary Vault",
      "responsible": "B1662",
      "servername": "sv00549"
    },
    {
      "applier": "S18344",
      "id": 550,
      "owner": "B1662",
      "purpose": "CyberArk Prod - Secondary Vault",
      "responsible": "B1662",
      "servername": "sv00550"
    },
    {
      "applier": "S18344",
      "id": 551,
      "owner": "B1662",
      "purpose": "CyberArk Prod - DR Vault",
      "responsible": "B1662",
      "servername": "sv00551"
    },
    {
      "applier": "M2129",
      "id": 552,
      "owner": "M2129",
      "purpose": "NON EPOS PrintServer",
      "responsible": "M2129",
      "servername": "sv00552"
    },
    {
      "applier": "S18344",
      "id": 553,
      "owner": "F0327",
      "purpose": "EPOS Print Server",
      "responsible": "S18344",
      "servername": "sv00553"
    },
    {
      "applier": "S18344",
      "id": 554,
      "owner": "F0327",
      "purpose": "EPOS Print Server",
      "responsible": "S18344",
      "servername": "sv00554"
    },
    {
      "applier": "S18344",
      "id": 555,
      "owner": "F0327",
      "purpose": "EPOS Print Server",
      "responsible": "S18344",
      "servername": "sv00555"
    },
    {
      "applier": "S18344",
      "id": 556,
      "owner": "F0327",
      "purpose": "EPOS Print Server",
      "responsible": "S18344",
      "servername": "sv00556"
    },
    {
      "applier": "S13571",
      "id": 557,
      "owner": "S13571",
      "purpose": "Siemens RTS/CFE 1",
      "responsible": "S13571",
      "servername": "sv00557"
    },
    {
      "applier": "S13571",
      "id": 558,
      "owner": "S13571",
      "purpose": "Siemens RTS/CFE 2",
      "responsible": "S13571",
      "servername": "sv00558"
    },
    {
      "applier": "S13571",
      "id": 559,
      "owner": "S13571",
      "purpose": "Siemens PSOS",
      "responsible": "S13571",
      "servername": "sv00559"
    },
    {
      "applier": "S13571",
      "id": 560,
      "owner": "S13571",
      "purpose": "Siemens OPM",
      "responsible": "S13571",
      "servername": "sv00560"
    },
    {
      "applier": "S18344",
      "id": 561,
      "owner": "S18344",
      "purpose": "Cisco IMC Supervisor",
      "responsible": "S18344",
      "servername": "sv00561"
    },
    {
      "applier": "A1912",
      "id": 562,
      "owner": "O1854",
      "purpose": "ASP HW Terminalserver",
      "responsible": "A1912",
      "servername": "sv00562"
    },
    {
      "applier": "A1912",
      "id": 563,
      "owner": "O1854",
      "purpose": "ASP HW Terminalserver",
      "responsible": "A1912",
      "servername": "sv00563"
    },
    {
      "applier": "A1912",
      "id": 564,
      "owner": "O1854",
      "purpose": "ASP HW Terminalserver",
      "responsible": "A1912",
      "servername": "sv00564"
    },
    {
      "applier": "A1912",
      "id": 565,
      "owner": "O1854",
      "purpose": "ASP HW Terminalserver",
      "responsible": "A1912",
      "servername": "sv00565"
    },
    {
      "applier": "A1912",
      "id": 566,
      "owner": "O1854",
      "purpose": "ASP HW Terminalserver",
      "responsible": "A1912",
      "servername": "sv00566"
    },
    {
      "applier": "A1912",
      "id": 567,
      "owner": "O1854",
      "purpose": "ASP HW Terminalserver",
      "responsible": "A1912",
      "servername": "sv00567"
    },
    {
      "applier": "A1912",
      "id": 568,
      "owner": "O1854",
      "purpose": "ASP HW Terminalserver",
      "responsible": "A1912",
      "servername": "sv00568"
    },
    {
      "applier": "A1912",
      "id": 569,
      "owner": "O1854",
      "purpose": "ASP HW Terminalserver",
      "responsible": "A1912",
      "servername": "sv00569"
    },
    {
      "applier": "A1912",
      "id": 570,
      "owner": "O1854",
      "purpose": "ASP HW Terminalserver",
      "responsible": "A1912",
      "servername": "sv00570"
    },
    {
      "applier": "A1912",
      "id": 571,
      "owner": "O1854",
      "purpose": "ASP HW Terminalserver",
      "responsible": "A1912",
      "servername": "sv00571"
    },
    {
      "applier": "A1912",
      "id": 572,
      "owner": "O1854",
      "purpose": "ASP HW Terminalserver",
      "responsible": "A1912",
      "servername": "sv00572"
    },
    {
      "applier": "A1912",
      "id": 573,
      "owner": "O1854",
      "purpose": "ASP HW Terminalserver",
      "responsible": "A1912",
      "servername": "sv00573"
    },
    {
      "applier": "D18268",
      "id": 574,
      "owner": "C10477",
      "purpose": "PoC Spectrum4VE",
      "responsible": "D18268",
      "servername": "sv00574"
    },
    {
      "applier": "D18268",
      "id": 575,
      "owner": "C10477",
      "purpose": "PoC Spectrum4VE-2",
      "responsible": "D18268",
      "servername": "sv00575"
    },
    {
      "applier": "T15463",
      "id": 576,
      "owner": "S19285",
      "purpose": "Microsoft Orchestrator DEV",
      "responsible": "T15463",
      "servername": "sv00576"
    },
    {
      "applier": "T15463",
      "id": 577,
      "owner": "J0649",
      "purpose": "Windows Server for File Service Worms [DFS-R]",
      "responsible": "J0649",
      "servername": "sv00577"
    },
    {
      "applier": "T15463",
      "id": 578,
      "owner": "J0649",
      "purpose": "\tWindows Server for File Service Worms [DFS-R]",
      "responsible": "J0649",
      "servername": "sv00578"
    },
    {
      "applier": "T15463",
      "id": 579,
      "owner": "J0649",
      "purpose": "Fileserver for Project Sand Day 1",
      "responsible": "J0649",
      "servername": "sv00579"
    },
    {
      "applier": "A0423",
      "id": 580,
      "owner": "M2474",
      "purpose": "Appliance for scanning of Lotus Notes",
      "responsible": "A0423",
      "servername": "sv00580"
    },
    {
      "applier": "T15463",
      "id": 581,
      "owner": "B6833",
      "purpose": "WAS-0200 Tomcat Shared Platform - Production",
      "responsible": "T15463",
      "servername": "sv00581"
    },
    {
      "applier": "T15463",
      "id": 582,
      "owner": "B6833",
      "purpose": "WAS-0200 Tomcat Shared Platform - Production",
      "responsible": "T15463",
      "servername": "sv00582"
    },
    {
      "applier": "T15463",
      "id": 583,
      "owner": "B6833",
      "purpose": "WAS-0200 Tomcat Shared Platform - Production",
      "responsible": "T15463",
      "servername": "sv00583"
    },
    {
      "applier": "T15463",
      "id": 584,
      "owner": "B6833",
      "purpose": "WAS-0200 Tomcat Shared Platform - Production",
      "responsible": "T15463",
      "servername": "sv00584"
    },
    {
      "applier": "T15463",
      "id": 585,
      "owner": "B6833",
      "purpose": "WAS-0200 Tomcat Shared Platform - Production",
      "responsible": "T15463",
      "servername": "sv00585"
    },
    {
      "applier": "T15463",
      "id": 586,
      "owner": "B6833",
      "purpose": "WAS-0200 Tomcat Shared Platform - Production",
      "responsible": "T15463",
      "servername": "sv00586"
    },
    {
      "applier": "S13571",
      "id": 587,
      "owner": "S13571",
      "purpose": "VMware Host - PLS Worms",
      "responsible": "S13571",
      "servername": "sv00587"
    },
    {
      "applier": "S13571",
      "id": 588,
      "owner": "S13571",
      "purpose": "VMware Host - PLS Worms",
      "responsible": "S13571",
      "servername": "sv00588"
    },
    {
      "applier": "M39546",
      "id": 589,
      "owner": "C10586",
      "purpose": "Priva Geb\u00c3\u00a4udeleittechnik",
      "responsible": "M39546",
      "servername": "sv00589"
    },
    {
      "applier": "H1863",
      "id": 590,
      "owner": "M3697",
      "purpose": "Test environment for new File Service concept",
      "responsible": "M3697",
      "servername": "sv00590"
    },
    {
      "applier": "O0067",
      "id": 591,
      "owner": "D1332",
      "purpose": "essm",
      "responsible": "O0067",
      "servername": "sv00591"
    },
    {
      "applier": "D18268",
      "id": 592,
      "owner": "K12285",
      "purpose": "NDES f\u00c3\u00bcr EPOS Projekt",
      "responsible": "D18268",
      "servername": "sv00592"
    },
    {
      "applier": "O0067",
      "id": 593,
      "owner": "A1019",
      "purpose": "Mobile Devices Management Server BES12",
      "responsible": "O0067",
      "servername": "sv00593"
    },
    {
      "applier": "T15463",
      "id": 594,
      "owner": "B6833",
      "purpose": "Workbook Application Server",
      "responsible": "T15463",
      "servername": "sv00594"
    },
    {
      "applier": "T15463",
      "id": 595,
      "owner": "B6833",
      "purpose": "Workbook Application Server",
      "responsible": "T15463",
      "servername": "sv00595"
    },
    {
      "applier": "T15463",
      "id": 596,
      "owner": "B6833",
      "purpose": "Foundation Server",
      "responsible": "T15463",
      "servername": "sv00596"
    },
    {
      "applier": "T15463",
      "id": 597,
      "owner": "B6833",
      "purpose": "Foundation Server",
      "responsible": "T15463",
      "servername": "sv00597"
    },
    {
      "applier": "T15463",
      "id": 598,
      "owner": "B6833",
      "purpose": "HUB-Server",
      "responsible": "T15463",
      "servername": "sv00598"
    },
    {
      "applier": "T15463",
      "id": 599,
      "owner": "B6833",
      "purpose": "HUB-Server",
      "responsible": "T15463",
      "servername": "sv00599"
    },
    {
      "applier": "T15463",
      "id": 600,
      "owner": "B6833",
      "purpose": "CISPro Server",
      "responsible": "T15463",
      "servername": "sv00600"
    },
    {
      "applier": "T15463",
      "id": 601,
      "owner": "B6833",
      "purpose": "CISPro Server",
      "responsible": "T15463",
      "servername": "sv00601"
    },
    {
      "applier": "B13085",
      "id": 602,
      "owner": "J0649",
      "purpose": "Fileserver for Project &quot;Sand&quot;",
      "responsible": "B13085",
      "servername": "sv00602"
    },
    {
      "applier": "T15463",
      "id": 603,
      "owner": "T0549",
      "purpose": "WAS-1300 New BO Platform for YW1",
      "responsible": "T15463",
      "servername": "sv00603"
    },
    {
      "applier": "A0423",
      "id": 604,
      "owner": "J0465",
      "purpose": "TSM Server Antwerpen",
      "responsible": "A0423",
      "servername": "sv00604"
    },
    {
      "applier": "A0423",
      "id": 605,
      "owner": "J0465",
      "purpose": "P2000G3 iSCSI",
      "responsible": "A0423",
      "servername": "sv00605"
    },
    {
      "applier": "A0423",
      "id": 606,
      "owner": "J0465",
      "purpose": "P2000G3 iSCSI",
      "responsible": "A0423",
      "servername": "sv00606"
    },
    {
      "applier": "A0423",
      "id": 607,
      "owner": "J0465",
      "purpose": "P2000G3 iSCSI",
      "responsible": "A0423",
      "servername": "sv00607"
    },
    {
      "applier": "A0423",
      "id": 608,
      "owner": "J0465",
      "purpose": "P2000G3 iSCSI",
      "responsible": "A0423",
      "servername": "sv00608"
    },
    {
      "applier": "D18268",
      "id": 609,
      "owner": "D1332",
      "purpose": "Secure Evonik File transfer",
      "responsible": "D18268",
      "servername": "sv00609"
    },
    {
      "applier": "A0423",
      "id": 610,
      "owner": "G0436",
      "purpose": "Softgate Server Hanau",
      "responsible": "A0423",
      "servername": "sv00610"
    },
    {
      "applier": "A0423",
      "id": 611,
      "owner": "G0436",
      "purpose": "Softgate Server Hanau",
      "responsible": "A0423",
      "servername": "sv00611"
    },
    {
      "applier": "D18268",
      "id": 612,
      "owner": "D1332",
      "purpose": "Secure Evonik File Transfer",
      "responsible": "D18268",
      "servername": "sv00612"
    },
    {
      "applier": "B13085",
      "id": 613,
      "owner": "S1248",
      "purpose": "SYSPRO-Applikation",
      "responsible": "B13085",
      "servername": "sv00613"
    },
    {
      "applier": "T15463",
      "id": 614,
      "owner": "M23734",
      "purpose": "Pre-Dev/Sandbox server for the OpenText Landscape",
      "responsible": "T15463",
      "servername": "sv00614"
    },
    {
      "applier": "J23543",
      "id": 615,
      "owner": "J23543",
      "purpose": "NAJ production jump server in DMZ",
      "responsible": "J23543",
      "servername": "sv00615"
    },
    {
      "applier": "J23543",
      "id": 616,
      "owner": "J23543",
      "purpose": "NAJ production jump server in DMZ",
      "responsible": "J23543",
      "servername": "sv00616"
    },
    {
      "applier": "B13085",
      "id": 617,
      "owner": "O1854",
      "purpose": "APP ASP-Server for the location Hanau (WOL)",
      "responsible": "B13085",
      "servername": "sv00617"
    },
    {
      "applier": "B13085",
      "id": 618,
      "owner": "O1854",
      "purpose": "APP ASP-Server for the location Hanau (WOL)",
      "responsible": "B13085",
      "servername": "sv00618"
    },
    {
      "applier": "D18268",
      "id": 619,
      "owner": "M23055",
      "purpose": "Informatica PIM Migration",
      "responsible": "D18268",
      "servername": "sv00619"
    },
    {
      "applier": "D18268",
      "id": 620,
      "owner": "M23055",
      "purpose": "Informatica PIM Migration.",
      "responsible": "D18268",
      "servername": "sv00620"
    },
    {
      "applier": "S0344",
      "id": 621,
      "owner": "S0344",
      "purpose": "vROPS Master",
      "responsible": "S0344",
      "servername": "sv00621"
    },
    {
      "applier": "S0344",
      "id": 622,
      "owner": "S0344",
      "purpose": "vROPS Collector EMEA",
      "responsible": "S0344",
      "servername": "sv00622"
    },
    {
      "applier": "S0344",
      "id": 623,
      "owner": "S0344",
      "purpose": "vROPS Collector AMERICAS",
      "responsible": "S0344",
      "servername": "sv00623"
    },
    {
      "applier": "S0344",
      "id": 624,
      "owner": "S0344",
      "purpose": "vROPS Collector ASIA",
      "responsible": "S0344",
      "servername": "sv00624"
    },
    {
      "applier": "S0344",
      "id": 625,
      "owner": "S0344",
      "purpose": "vROPS Collector QA",
      "responsible": "S0344",
      "servername": "sv00625"
    },
    {
      "applier": "T15463",
      "id": 626,
      "owner": "F1768",
      "purpose": "SQL - FRA3",
      "responsible": "T15463",
      "servername": "sv00626"
    },
    {
      "applier": "T15463",
      "id": 627,
      "owner": "F1768",
      "purpose": "SQL - FRA3",
      "responsible": "T15463",
      "servername": "sv00627"
    },
    {
      "applier": "T15463",
      "id": 628,
      "owner": "F1768",
      "purpose": "SQL - FRA3",
      "responsible": "T15463",
      "servername": "sv00628"
    },
    {
      "applier": "T15463",
      "id": 629,
      "owner": "F1768",
      "purpose": "SQL - FRA3",
      "responsible": "T15463",
      "servername": "sv00629"
    },
    {
      "applier": "T15463",
      "id": 630,
      "owner": "F1768",
      "purpose": "SQL - FRA3",
      "responsible": "T15463",
      "servername": "sv00630"
    },
    {
      "applier": "T15463",
      "id": 631,
      "owner": "F1768",
      "purpose": "SQL - FRA3",
      "responsible": "T15463",
      "servername": "sv00631"
    },
    {
      "applier": "B13085",
      "id": 632,
      "owner": "B11210",
      "purpose": "DC-Background_Process_Server",
      "responsible": "B13085",
      "servername": "sv00632"
    },
    {
      "applier": "A0423",
      "id": 633,
      "owner": "G0806",
      "purpose": "Softgate Server Essen",
      "responsible": "A0423",
      "servername": "sv00633"
    },
    {
      "applier": "T15463",
      "id": 634,
      "owner": "R1138",
      "purpose": "Application",
      "responsible": "T15463",
      "servername": "sv00634"
    },
    {
      "applier": "J0649",
      "id": 635,
      "owner": "M3697",
      "purpose": "Test-Environment",
      "responsible": "J0649",
      "servername": "sv00635"
    },
    {
      "applier": "J0649",
      "id": 636,
      "owner": "M3697",
      "purpose": "Test-Environment",
      "responsible": "J0649",
      "servername": "sv00636"
    },
    {
      "applier": "J0649",
      "id": 637,
      "owner": "M3697",
      "purpose": "Test-Environment",
      "responsible": "J0649",
      "servername": "sv00637"
    },
    {
      "applier": "J0649",
      "id": 638,
      "owner": "M3697",
      "purpose": "Test-Environment",
      "responsible": "J0649",
      "servername": "sv00638"
    },
    {
      "applier": "B13085",
      "id": 639,
      "owner": "M23055",
      "purpose": "App Server for MDO",
      "responsible": "B13085",
      "servername": "sv00639"
    },
    {
      "applier": "B13085",
      "id": 640,
      "owner": "M23055",
      "purpose": "New App Server MDO Marl",
      "responsible": "B13085",
      "servername": "sv00640"
    },
    {
      "applier": "B13085",
      "id": 641,
      "owner": "B6833",
      "purpose": "AM-Development",
      "responsible": "B13085",
      "servername": "sv00641"
    },
    {
      "applier": "B13085",
      "id": 642,
      "owner": "I0378",
      "purpose": "New Server for Antwerpen",
      "responsible": "B13085",
      "servername": "sv00642"
    },
    {
      "applier": "B13085",
      "id": 643,
      "owner": "C7216",
      "purpose": " Server for PIMS System",
      "responsible": "B13085",
      "servername": "sv00643"
    },
    {
      "applier": "h17255",
      "id": 644,
      "owner": "H17255",
      "purpose": "VCE",
      "responsible": "H17255",
      "servername": "sv00644"
    },
    {
      "applier": "S0344",
      "id": 645,
      "owner": "S0344",
      "purpose": "vROPS Collector EMEA",
      "responsible": "S0344",
      "servername": "sv00645"
    },
    {
      "applier": "S18344",
      "id": 646,
      "owner": "M0770",
      "purpose": "Simpati Server",
      "responsible": "S18344",
      "servername": "sv00646"
    },
    {
      "applier": "T15463",
      "id": 647,
      "owner": "J0649",
      "purpose": "File Server for Frankfurt ES1",
      "responsible": "T15463",
      "servername": "sv00647"
    },
    {
      "applier": "T15463",
      "id": 648,
      "owner": "J0649",
      "purpose": "File Server ES2 [new DC]",
      "responsible": "T15463",
      "servername": "sv00648"
    },
    {
      "applier": "S0344",
      "id": 649,
      "owner": "S0344",
      "purpose": "VMware vCenter PSC QA",
      "responsible": "S0344",
      "servername": "sv00649"
    },
    {
      "applier": "S0344",
      "id": 650,
      "owner": "S0344",
      "purpose": "VMware vCenter PSC 2 QA",
      "responsible": "S0344",
      "servername": "sv00650"
    },
    {
      "applier": "S0344",
      "id": 651,
      "owner": "S0344",
      "purpose": "VMware vCenter  QA",
      "responsible": "S0344",
      "servername": "sv00651"
    },
    {
      "applier": "D18268",
      "id": 652,
      "owner": "R0697",
      "purpose": "PIMS-System IP21 Bau 981",
      "responsible": "D18268",
      "servername": "sv00652"
    },
    {
      "applier": "D18268",
      "id": 653,
      "owner": "L0067",
      "purpose": "uCMDB Browser",
      "responsible": "D18268",
      "servername": "sv00653"
    },
    {
      "applier": "S26620",
      "id": 654,
      "owner": "D0321",
      "purpose": "PIMS Application",
      "responsible": "S26620",
      "servername": "sv00654"
    },
    {
      "applier": "D18268",
      "id": 655,
      "owner": "M38510",
      "purpose": "POC - CyberObserver",
      "responsible": "D18268",
      "servername": "sv00655"
    },
    {
      "applier": "s19749",
      "id": 656,
      "owner": "S19749",
      "purpose": "Citrix server",
      "responsible": "S19749",
      "servername": "sv00656"
    },
    {
      "applier": "T15463",
      "id": 657,
      "owner": "S0060",
      "purpose": "SP-0500 NOM",
      "responsible": "T15463",
      "servername": "sv00657"
    },
    {
      "applier": "T15463",
      "id": 658,
      "owner": "S0060",
      "purpose": "SP-0500 NOM",
      "responsible": "T15463",
      "servername": "sv00658"
    },
    {
      "applier": "T15463",
      "id": 659,
      "owner": "S0060",
      "purpose": "SP-0500 NOM",
      "responsible": "T15463",
      "servername": "sv00659"
    },
    {
      "applier": "T15463",
      "id": 660,
      "owner": "S0060",
      "purpose": "SP-0500 NOM",
      "responsible": "T15463",
      "servername": "sv00660"
    },
    {
      "applier": "D18268",
      "id": 661,
      "owner": "D1332",
      "purpose": "Secure Evonik File Transfer2",
      "responsible": "D18268",
      "servername": "sv00661"
    },
    {
      "applier": "T15463",
      "id": 662,
      "owner": "B1500",
      "purpose": "DataAggregator und DataRepositiory",
      "responsible": "T15463",
      "servername": "sv00662"
    },
    {
      "applier": "B13085",
      "id": 663,
      "owner": "I0240",
      "purpose": "Virtueller Server f\u00c3\u00bcr Compass Prodnetz",
      "responsible": "B13085",
      "servername": "sv00663"
    },
    {
      "applier": "T15463",
      "id": 664,
      "owner": "A1019",
      "purpose": "BlackBerry BES12 UEM 12.7",
      "responsible": "T15463",
      "servername": "sv00664"
    },
    {
      "applier": "T15463",
      "id": 665,
      "owner": "A0751",
      "purpose": "Cluster ",
      "responsible": "T15463",
      "servername": "sv00665"
    },
    {
      "applier": "B13085",
      "id": 666,
      "owner": "I0240",
      "purpose": "Compass",
      "responsible": "B13085",
      "servername": "sv00666"
    },
    {
      "applier": "B13085",
      "id": 667,
      "owner": "C0352",
      "purpose": "Projekt SIDAP",
      "responsible": "B13085",
      "servername": "sv00667"
    },
    {
      "applier": "Y5011",
      "id": 668,
      "owner": "O1854",
      "purpose": "APP ASP-Server ",
      "responsible": "Y5011",
      "servername": "sv00668"
    },
    {
      "applier": "D18268",
      "id": 669,
      "owner": "M39456",
      "purpose": "Route Explorer",
      "responsible": "D18268",
      "servername": "sv00669"
    },
    {
      "applier": "D18268",
      "id": 670,
      "owner": "R15590",
      "purpose": "PIMS Server",
      "responsible": "D18268",
      "servername": "sv00670"
    },
    {
      "applier": "D18268",
      "id": 671,
      "owner": "R15590",
      "purpose": "PIMS Server - 2",
      "responsible": "D18268",
      "servername": "sv00671"
    },
    {
      "applier": "D18268",
      "id": 672,
      "owner": "R15590",
      "purpose": "PIMS Server - 3",
      "responsible": "D18268",
      "servername": "sv00672"
    },
    {
      "applier": "S26686",
      "id": 673,
      "owner": "B6833",
      "purpose": "WAS-1300 New BO Platform for PW1",
      "responsible": "S26686",
      "servername": "sv00673"
    },
    {
      "applier": "S26686",
      "id": 674,
      "owner": "B6833",
      "purpose": "WAS-1300 New BO Platform for PW1",
      "responsible": "S26686",
      "servername": "sv00674"
    },
    {
      "applier": "H1863",
      "id": 675,
      "owner": "F0327",
      "purpose": "EPOS Server DC (reinstallation of wol61510/ds3017)",
      "responsible": "F0327",
      "servername": "sv00675"
    },
    {
      "applier": "H1863",
      "id": 676,
      "owner": "F0327",
      "purpose": "EPOS Server DC (reinstallation of wol61511/ds3018)",
      "responsible": "F0327",
      "servername": "sv00676"
    },
    {
      "applier": "S26686",
      "id": 677,
      "owner": "B6833",
      "purpose": "BO WAS-1300 for QW1",
      "responsible": "S26686",
      "servername": "sv00677"
    },
    {
      "applier": "S26686",
      "id": 678,
      "owner": "B6833",
      "purpose": "BO WAS-1300 for QW1",
      "responsible": "S26686",
      "servername": "sv00678"
    },
    {
      "applier": "S26620",
      "id": 679,
      "owner": "T12969",
      "purpose": "Finito Application",
      "responsible": "S26620",
      "servername": "sv00679"
    },
    {
      "applier": "S0344",
      "id": 680,
      "owner": "S1728",
      "purpose": "PIMS WOR",
      "responsible": "S0344",
      "servername": "sv00680"
    },
    {
      "applier": "D18268",
      "id": 681,
      "owner": "C0930",
      "purpose": "WSUS for EDIS System",
      "responsible": "D18268",
      "servername": "sv00681"
    },
    {
      "applier": "D18268",
      "id": 682,
      "owner": "O1854",
      "purpose": "APP ASP-Server",
      "responsible": "D18268",
      "servername": "sv00682"
    },
    {
      "applier": "D18268",
      "id": 683,
      "owner": "O1854",
      "purpose": "APP ASP-Server2",
      "responsible": "D18268",
      "servername": "sv00683"
    },
    {
      "applier": "S26686",
      "id": 684,
      "owner": "R0930",
      "purpose": "Microsoft Deployment Toolkit",
      "responsible": "S26686",
      "servername": "sv00684"
    },
    {
      "applier": "Y5011",
      "id": 685,
      "owner": "P11600",
      "purpose": "DAKS Server ",
      "responsible": "Y5011",
      "servername": "sv00685"
    },
    {
      "applier": "Y5011",
      "id": 686,
      "owner": "L8858",
      "purpose": "server for Jenkins implementation",
      "responsible": "Y5011",
      "servername": "sv00686"
    },
    {
      "applier": "T15463",
      "id": 687,
      "owner": "M6364",
      "purpose": "CSM FRA1 ",
      "responsible": "T15463",
      "servername": "sv00687"
    },
    {
      "applier": "S26620",
      "id": 688,
      "owner": "B6833",
      "purpose": "WAS-1300 New BO Platform for DW1",
      "responsible": "S26620",
      "servername": "sv00688"
    },
    {
      "applier": "S26620",
      "id": 689,
      "owner": "B6833",
      "purpose": "WAS-1300 New BO Platform for DW1",
      "responsible": "S26620",
      "servername": "sv00689"
    },
    {
      "applier": "S18344",
      "id": 690,
      "owner": "F1768",
      "purpose": "Oracle Database Server",
      "responsible": "S18344",
      "servername": "sv00690"
    },
    {
      "applier": "S18344",
      "id": 691,
      "owner": "F1768",
      "purpose": "Oracle Database Server",
      "responsible": "S18344",
      "servername": "sv00691"
    },
    {
      "applier": "S18344",
      "id": 692,
      "owner": "F1768",
      "purpose": "MS SQL Server",
      "responsible": "S18344",
      "servername": "sv00692"
    },
    {
      "applier": "S18344",
      "id": 693,
      "owner": "F1768",
      "purpose": "MS SQL Server",
      "responsible": "S18344",
      "servername": "sv00693"
    },
    {
      "applier": "S0344",
      "id": 694,
      "owner": "S0344",
      "purpose": "VMware Capacity Planner",
      "responsible": "S0344",
      "servername": "sv00694"
    },
    {
      "applier": "S0344",
      "id": 695,
      "owner": "S0344",
      "purpose": "VMware Capacity Planner",
      "responsible": "S0344",
      "servername": "sv00695"
    },
    {
      "applier": "D18268",
      "id": 696,
      "owner": "W10990",
      "purpose": "PIMS AO",
      "responsible": "D18268",
      "servername": "sv00696"
    },
    {
      "applier": "T15463",
      "id": 697,
      "owner": "I4738",
      "purpose": " BO server to replace ANT1106",
      "responsible": "T15463",
      "servername": "sv00697"
    },
    {
      "applier": "T15463",
      "id": 698,
      "owner": "M23734",
      "purpose": "Vertex upgrade project",
      "responsible": "T15463",
      "servername": "sv00698"
    },
    {
      "applier": "D18268",
      "id": 699,
      "owner": "A1019",
      "purpose": "Blackberry BES12",
      "responsible": "D18268",
      "servername": "sv00699"
    },
    {
      "applier": "Y5011",
      "id": 700,
      "owner": "A22929",
      "purpose": "Web Server",
      "responsible": "Y5011",
      "servername": "sv00700"
    },
    {
      "applier": "T15463",
      "id": 701,
      "owner": "T0389",
      "purpose": "Office 365 Reporting Server",
      "responsible": "T15463",
      "servername": "sv00701"
    },
    {
      "applier": "R21409",
      "id": 702,
      "owner": "D9446",
      "purpose": "Event management environment.",
      "responsible": "R21409",
      "servername": "sv00702"
    },
    {
      "applier": "R21409",
      "id": 703,
      "owner": "D9446",
      "purpose": "Event management environment.",
      "responsible": "R21409",
      "servername": "sv00703"
    },
    {
      "applier": "X0682",
      "id": 704,
      "owner": "X0682",
      "purpose": "Jump Server for Signal DCS",
      "responsible": "X0682",
      "servername": "sv00704"
    },
    {
      "applier": "S26686",
      "id": 705,
      "owner": "D9446",
      "purpose": "Event Management",
      "responsible": "S26686",
      "servername": "sv00705"
    },
    {
      "applier": "D18268",
      "id": 706,
      "owner": "M6364",
      "purpose": "Server CSM",
      "responsible": "D18268",
      "servername": "sv00706"
    },
    {
      "applier": "B13085",
      "id": 707,
      "owner": "M30705",
      "purpose": "VM Compass",
      "responsible": "D18268",
      "servername": "sv00707"
    },
    {
      "applier": "T15463",
      "id": 708,
      "owner": "T8973",
      "purpose": "Web-Basis",
      "responsible": "T15463",
      "servername": "sv00708"
    },
    {
      "applier": "T15463",
      "id": 709,
      "owner": "T8973",
      "purpose": "Web-Basis",
      "responsible": "T15463",
      "servername": "sv00709"
    },
    {
      "applier": "S26620",
      "id": 710,
      "owner": "B6833",
      "purpose": "WAS-0200 Tomcat Integration",
      "responsible": "S26620",
      "servername": "sv00710"
    },
    {
      "applier": "C1314",
      "id": 711,
      "owner": "M3697",
      "purpose": "Key Management Server 2016",
      "responsible": "M3697",
      "servername": "sv00711"
    },
    {
      "applier": "G12866",
      "id": 712,
      "owner": "E8628",
      "purpose": "Windows MBAM Service",
      "responsible": "G12866",
      "servername": "sv00712"
    },
    {
      "applier": "Y5011",
      "id": 713,
      "owner": "D10569",
      "purpose": "RFT00423292",
      "responsible": "Y5011",
      "servername": "sv00713"
    },
    {
      "applier": "S26620",
      "id": 714,
      "owner": "D0907",
      "purpose": " EPO/ENS Server",
      "responsible": "S26620",
      "servername": "sv00714"
    },
    {
      "applier": "S26620",
      "id": 715,
      "owner": "D0907",
      "purpose": "EPO/ENS Server",
      "responsible": "S26620",
      "servername": "sv00715"
    },
    {
      "applier": "S13571",
      "id": 716,
      "owner": "S13571",
      "purpose": "Isilon InsightIQ",
      "responsible": "S13571",
      "servername": "sv00716"
    },
    {
      "applier": "S26620",
      "id": 717,
      "owner": "C10586",
      "purpose": "Fileserver for PMMA Operation",
      "responsible": "S26620",
      "servername": "sv00717"
    },
    {
      "applier": "Y5011",
      "id": 718,
      "owner": "O0371",
      "purpose": "RFT00429241",
      "responsible": "Y5011",
      "servername": "sv00718"
    },
    {
      "applier": "S26686",
      "id": 719,
      "owner": "J0231",
      "purpose": "Plastics-Database",
      "responsible": "S26686",
      "servername": "sv00719"
    },
    {
      "applier": "R21409",
      "id": 720,
      "owner": "T3070",
      "purpose": "DC2016+ Go WP2 Relocation_____IPMS ",
      "responsible": "R21409",
      "servername": "sv00720"
    },
    {
      "applier": "R21409",
      "id": 721,
      "owner": "T3070",
      "purpose": "DC2016+ Go WP2 Relocation_____IPMS ",
      "responsible": "R21409",
      "servername": "sv00721"
    },
    {
      "applier": "R21409",
      "id": 722,
      "owner": "T3070",
      "purpose": "DC2016+ Go WP2 Relocation_____IPMS",
      "responsible": "R21409",
      "servername": "sv00722"
    },
    {
      "applier": "R21409",
      "id": 723,
      "owner": "B1500",
      "purpose": "New DC",
      "responsible": "R21409",
      "servername": "sv00723"
    },
    {
      "applier": "Y5011",
      "id": 724,
      "owner": "D1599",
      "purpose": "Equipment for the alarm management",
      "responsible": "Y5011",
      "servername": "sv00724"
    },
    {
      "applier": "S26686",
      "id": 725,
      "owner": "B11210",
      "purpose": "Appspace",
      "responsible": "S26686",
      "servername": "sv00725"
    },
    {
      "applier": "D18547",
      "id": 726,
      "owner": "I4738",
      "purpose": "W2KR12 SQL Server",
      "responsible": "D18547",
      "servername": "sv00726"
    },
    {
      "applier": "S18344",
      "id": 727,
      "owner": "S18344",
      "purpose": "itsm-QA-ALM ",
      "responsible": "S18344",
      "servername": "sv00727"
    },
    {
      "applier": "T15463",
      "id": 728,
      "owner": "M31826",
      "purpose": "QA server Vertex upgrade project",
      "responsible": "T15463",
      "servername": "sv00728"
    },
    {
      "applier": "G12866",
      "id": 729,
      "owner": "S1879",
      "purpose": "Fileserver PLS DMZ",
      "responsible": "G12866",
      "servername": "sv00729"
    },
    {
      "applier": "S26620",
      "id": 730,
      "owner": "K17867",
      "purpose": "Win10 AppDNA Serversystem",
      "responsible": "S26620",
      "servername": "sv00730"
    },
    {
      "applier": "R21409",
      "id": 731,
      "owner": "C1181",
      "purpose": "SAP Cloud Connectors",
      "responsible": "R21409",
      "servername": "sv00731"
    },
    {
      "applier": "R21409",
      "id": 732,
      "owner": "C1181",
      "purpose": "SAP Cloud Connectors",
      "responsible": "R21409",
      "servername": "sv00732"
    },
    {
      "applier": "m39382",
      "id": 733,
      "owner": "S19749",
      "purpose": "XenApp/XenDesktop Delivery Controller version 7.15",
      "responsible": "M39382",
      "servername": "sv00733"
    },
    {
      "applier": "M39382",
      "id": 734,
      "owner": "S19749",
      "purpose": "XenApp/XenDesktop Delivery Controller version 7.15",
      "responsible": "M39382",
      "servername": "sv00734"
    },
    {
      "applier": "S26686",
      "id": 735,
      "owner": "M34002",
      "purpose": "New SQL Server",
      "responsible": "S26686",
      "servername": "sv00735"
    },
    {
      "applier": "S18344",
      "id": 736,
      "owner": "S18344",
      "purpose": "SMW-SO FG-AUTO Scripting Appliance",
      "responsible": "S18344",
      "servername": "sv00736"
    },
    {
      "applier": "S18344",
      "id": 737,
      "owner": "S18344",
      "purpose": "SMW-SO FG-AUTO Scripting Server",
      "responsible": "S18344",
      "servername": "sv00737"
    },
    {
      "applier": "B13085",
      "id": 738,
      "owner": "J0649",
      "purpose": "Serverrequest by J\u00c3\u00bcrgen Stocks",
      "responsible": "B13085",
      "servername": "sv00738"
    },
    {
      "applier": "T15463",
      "id": 739,
      "owner": "F10661",
      "purpose": " Projekt Tours",
      "responsible": "T15463",
      "servername": "sv00739"
    },
    {
      "applier": "S18344",
      "id": 740,
      "owner": "O1854",
      "purpose": "ASP Terminal Server Steinau",
      "responsible": "S18344",
      "servername": "sv00740"
    },
    {
      "applier": "S18344",
      "id": 741,
      "owner": "O1854",
      "purpose": "\tASP Terminal Server Steinau",
      "responsible": "S18344",
      "servername": "sv00741"
    },
    {
      "applier": "D18269",
      "id": 742,
      "owner": "J0649",
      "purpose": "New Fileserver for Lenzing",
      "responsible": "D18269",
      "servername": "sv00742"
    },
    {
      "applier": "T15463",
      "id": 743,
      "owner": "S20376",
      "purpose": "Reverse proxy webserver for Evonik Smart Touch",
      "responsible": "T15463",
      "servername": "sv00743"
    },
    {
      "applier": "S26686",
      "id": 744,
      "owner": "R0644",
      "purpose": "RFT00442958",
      "responsible": "S26686",
      "servername": "sv00744"
    },
    {
      "applier": "S0344",
      "id": 745,
      "owner": "S0344",
      "purpose": "HP Oneview",
      "responsible": "S0344",
      "servername": "sv00745"
    },
    {
      "applier": "S26686",
      "id": 746,
      "owner": "T8973",
      "purpose": "Citrix XenDesktop/XenApp Delivery Controller PROD",
      "responsible": "S26686",
      "servername": "sv00746"
    },
    {
      "applier": "S26686",
      "id": 747,
      "owner": "T8973",
      "purpose": "Citrix XenDesktop/XenApp Delivery Controller PROD",
      "responsible": "S26686",
      "servername": "sv00747"
    },
    {
      "applier": "S26620",
      "id": 748,
      "owner": "A0905",
      "purpose": "Server for application BlueControl ",
      "responsible": "S26620",
      "servername": "sv00748"
    },
    {
      "applier": "T15463",
      "id": 749,
      "owner": "E9905",
      "purpose": "For MCC",
      "responsible": "T15463",
      "servername": "sv00749"
    },
    {
      "applier": "T15463",
      "id": 750,
      "owner": "E9905",
      "purpose": "For MCC",
      "responsible": "T15463",
      "servername": "sv00750"
    },
    {
      "applier": "S26686",
      "id": 751,
      "owner": "R14077",
      "purpose": "RFT00436745",
      "responsible": "S26686",
      "servername": "sv00751"
    },
    {
      "applier": "S26620",
      "id": 752,
      "owner": "I0652",
      "purpose": "McAfee Content Security Reporter",
      "responsible": "S26620",
      "servername": "sv00752"
    },
    {
      "applier": "S0344",
      "id": 753,
      "owner": "S0344",
      "purpose": "HPE ILO Amplifier",
      "responsible": "S0344",
      "servername": "sv00753"
    },
    {
      "applier": "S0344",
      "id": 754,
      "owner": "S0344",
      "purpose": "HPSIM",
      "responsible": "S0344",
      "servername": "sv00754"
    },
    {
      "applier": "S0344",
      "id": 755,
      "owner": "S0344",
      "purpose": "SQL Server POD",
      "responsible": "S0344",
      "servername": "sv00755"
    },
    {
      "applier": "T15463",
      "id": 756,
      "owner": "S20376",
      "purpose": "WAS-5200",
      "responsible": "T15463",
      "servername": "sv00756"
    },
    {
      "applier": "T15463",
      "id": 757,
      "owner": "M23816",
      "purpose": "SP-0300 Enterprise Search",
      "responsible": "T15463",
      "servername": "sv00757"
    },
    {
      "applier": "O0067",
      "id": 758,
      "owner": "U0358",
      "purpose": "Grafana linux appliance",
      "responsible": "O0067",
      "servername": "sv00758"
    },
    {
      "applier": "S26686",
      "id": 759,
      "owner": "T8973",
      "purpose": "Application Control Center",
      "responsible": "S26686",
      "servername": "sv00759"
    },
    {
      "applier": "S26686",
      "id": 760,
      "owner": "T8973",
      "purpose": "Application Control Center",
      "responsible": "S26686",
      "servername": "sv00760"
    },
    {
      "applier": "T15463",
      "id": 761,
      "owner": "M23816",
      "purpose": " WAS-2300 HPPedia",
      "responsible": "T15463",
      "servername": "sv00761"
    },
    {
      "applier": "T15463",
      "id": 762,
      "owner": "M23816",
      "purpose": "WAS-2300 HPPedia",
      "responsible": "T15463",
      "servername": "sv00762"
    },
    {
      "applier": "B13085",
      "id": 763,
      "owner": "T3070",
      "purpose": "Projekt DSMS (Datenschutz Management System)",
      "responsible": "B13085",
      "servername": "sv00763"
    },
    {
      "applier": "S26686",
      "id": 764,
      "owner": "H1456",
      "purpose": "Reloc",
      "responsible": "S26686",
      "servername": "sv00764"
    },
    {
      "applier": "Y5011",
      "id": 765,
      "owner": "M2290",
      "purpose": "Jumpserver (Windows) for Network in FRA1",
      "responsible": "Y5011",
      "servername": "sv00765"
    },
    {
      "applier": "R21409",
      "id": 766,
      "owner": "M2290",
      "purpose": "Jumpserver (Windows) for Network in FRA3",
      "responsible": "R21409",
      "servername": "sv00766"
    },
    {
      "applier": "S26686",
      "id": 767,
      "owner": "M23055",
      "purpose": "Appilcation Server",
      "responsible": "S26686",
      "servername": "sv00767"
    },
    {
      "applier": "R21409",
      "id": 768,
      "owner": "B0163",
      "purpose": "OpenText Archiv Server",
      "responsible": "R21409",
      "servername": "sv00768"
    },
    {
      "applier": "T15463",
      "id": 769,
      "owner": "M23734",
      "purpose": "Vertex 8 upgrade project",
      "responsible": "T15463",
      "servername": "sv00769"
    },
    {
      "applier": "S26686",
      "id": 770,
      "owner": "J0143",
      "purpose": "Test Server",
      "responsible": "S26686",
      "servername": "sv00770"
    },
    {
      "applier": "S26686",
      "id": 771,
      "owner": "J0143",
      "purpose": "Production Server",
      "responsible": "S26686",
      "servername": "sv00771"
    },
    {
      "applier": "S26620",
      "id": 772,
      "owner": "L0346",
      "purpose": "Application Server",
      "responsible": "S26620",
      "servername": "sv00772"
    },
    {
      "applier": "S26620",
      "id": 773,
      "owner": "F8735",
      "purpose": "Virtual Appliance ISAM ",
      "responsible": "S26620",
      "servername": "sv00773"
    },
    {
      "applier": "S26686",
      "id": 774,
      "owner": "M23734",
      "purpose": "New Frankfurt Datacenter",
      "responsible": "S26686",
      "servername": "sv00774"
    },
    {
      "applier": "Y5011",
      "id": 775,
      "owner": "R1109",
      "purpose": "RDP CEGEKA Powershell scripts",
      "responsible": "Y5011",
      "servername": "sv00775"
    },
    {
      "applier": "S26686",
      "id": 776,
      "owner": "T8973",
      "purpose": "Application Control Center",
      "responsible": "S26686",
      "servername": "sv00776"
    },
    {
      "applier": "S26686",
      "id": 777,
      "owner": "S0295",
      "purpose": "RFT00464131",
      "responsible": "S26686",
      "servername": "sv00777"
    },
    {
      "applier": "S0344",
      "id": 778,
      "owner": "S0344",
      "purpose": "NVIDIA License Manager",
      "responsible": "S0344",
      "servername": "sv00778"
    },
    {
      "applier": "R21409",
      "id": 779,
      "owner": "D0106",
      "purpose": "SP4VE-Proxy ",
      "responsible": "R21409",
      "servername": "sv00779"
    },
    {
      "applier": "Y5011",
      "id": 780,
      "owner": "D0106",
      "purpose": "SP4VE-Proxy (min7.1.6.)   (ANT4VE02)  ",
      "responsible": "Y5011",
      "servername": "sv00780"
    },
    {
      "applier": "S26686",
      "id": 781,
      "owner": "S21771",
      "purpose": "RFT00473263",
      "responsible": "S26686",
      "servername": "sv00781"
    },
    {
      "applier": "S0344",
      "id": 782,
      "owner": "S0344",
      "purpose": "Domain Controller",
      "responsible": "S0344",
      "servername": "sv00782"
    },
    {
      "applier": "S0344",
      "id": 783,
      "owner": "S0344",
      "purpose": "Domain Controller",
      "responsible": "S0344",
      "servername": "sv00783"
    },
    {
      "applier": "S0344",
      "id": 784,
      "owner": "S0344",
      "purpose": "Domain Controller",
      "responsible": "S0344",
      "servername": "sv00784"
    },
    {
      "applier": "S0344",
      "id": 785,
      "owner": "S0344",
      "purpose": "Domain Controller",
      "responsible": "S0344",
      "servername": "sv00785"
    },
    {
      "applier": "S0344",
      "id": 786,
      "owner": "S0344",
      "purpose": "Domain Controller",
      "responsible": "S0344",
      "servername": "sv00786"
    },
    {
      "applier": "S0344",
      "id": 787,
      "owner": "S0344",
      "purpose": "ASP",
      "responsible": "S0344",
      "servername": "sv00787"
    },
    {
      "applier": "S0344",
      "id": 788,
      "owner": "S0344",
      "purpose": "ASP",
      "responsible": "S0344",
      "servername": "sv00788"
    },
    {
      "applier": "S0344",
      "id": 789,
      "owner": "S0344",
      "purpose": "ASP",
      "responsible": "S0344",
      "servername": "sv00789"
    },
    {
      "applier": "S0344",
      "id": 790,
      "owner": "S0344",
      "purpose": "ASP",
      "responsible": "S0344",
      "servername": "sv00790"
    },
    {
      "applier": "S0344",
      "id": 791,
      "owner": "S0344",
      "purpose": "USB Dongle Server",
      "responsible": "S0344",
      "servername": "sv00791"
    },
    {
      "applier": "S0344",
      "id": 792,
      "owner": "S0344",
      "purpose": "USB Dongle Server",
      "responsible": "S0344",
      "servername": "sv00792"
    },
    {
      "applier": "S0344",
      "id": 793,
      "owner": "S0344",
      "purpose": "IPMS",
      "responsible": "S0344",
      "servername": "sv00793"
    },
    {
      "applier": "S26686",
      "id": 794,
      "owner": "J22610",
      "purpose": "Software Test",
      "responsible": "S26686",
      "servername": "sv00794"
    },
    {
      "applier": "A0423",
      "id": 795,
      "owner": "A22929",
      "purpose": "Server &quot;ETL Metasonic &amp; Dashboard&quot;",
      "responsible": "A0423",
      "servername": "sv00795"
    },
    {
      "applier": "A0423",
      "id": 796,
      "owner": "A22029",
      "purpose": "Server &quot;QA_DEMO-Metasonic&quot;",
      "responsible": "A0423",
      "servername": "sv00796"
    },
    {
      "applier": "A0423",
      "id": 797,
      "owner": "A22929",
      "purpose": "Server &quot;DEV_DEMO-Metasonic&quot;",
      "responsible": "A0423",
      "servername": "sv00797"
    },
    {
      "applier": "S0344",
      "id": 798,
      "owner": "S0344",
      "purpose": "Analysis Information Leak Framework",
      "responsible": "S0344",
      "servername": "sv00798"
    },
    {
      "applier": "Y5011",
      "id": 799,
      "owner": "B11851",
      "purpose": "Small VM",
      "responsible": "Y5011",
      "servername": "sv00799"
    },
    {
      "applier": "S26686",
      "id": 800,
      "owner": "B1570",
      "purpose": "RFT00474978",
      "responsible": "S26686",
      "servername": "sv00800"
    },
    {
      "applier": "S26686",
      "id": 801,
      "owner": "C1181",
      "purpose": "RFT00475124",
      "responsible": "S26686",
      "servername": "sv00801"
    },
    {
      "applier": "S26686",
      "id": 802,
      "owner": "C1181",
      "purpose": "RFT00475124",
      "responsible": "S26686",
      "servername": "sv00802"
    },
    {
      "applier": "S0344",
      "id": 803,
      "owner": "S0344",
      "purpose": "MISP",
      "responsible": "S0344",
      "servername": "sv00803"
    },
    {
      "applier": "Y5011",
      "id": 804,
      "owner": "M23734",
      "purpose": "OpenText Landscape Upgrade",
      "responsible": "Y5011",
      "servername": "sv00804"
    },
    {
      "applier": "S26620",
      "id": 805,
      "owner": "M23734",
      "purpose": "OpenText landscape Server Prod",
      "responsible": "S26620",
      "servername": "sv00805"
    },
    {
      "applier": "S26620",
      "id": 806,
      "owner": "M23734",
      "purpose": "OpenText landscape Server QA",
      "responsible": "S26620",
      "servername": "sv00806"
    },
    {
      "applier": "S26620",
      "id": 807,
      "owner": "M23734",
      "purpose": "OpenText landscape Server DEV",
      "responsible": "S26620",
      "servername": "sv00807"
    },
    {
      "applier": "S26620",
      "id": 808,
      "owner": "M23734",
      "purpose": "OpenText landscape Server Prod",
      "responsible": "S26620",
      "servername": "sv00808"
    },
    {
      "applier": "S26620",
      "id": 809,
      "owner": "M23734",
      "purpose": "OpenText landscape Server Prod",
      "responsible": "S26620",
      "servername": "sv00809"
    },
    {
      "applier": "S26686",
      "id": 810,
      "owner": "T8973",
      "purpose": "Worker Core",
      "responsible": "S26686",
      "servername": "sv00810"
    },
    {
      "applier": "S26686",
      "id": 811,
      "owner": "T8973",
      "purpose": "Worker Core",
      "responsible": "S26686",
      "servername": "sv00811"
    },
    {
      "applier": "S26686",
      "id": 812,
      "owner": "T8973",
      "purpose": "Worker Core",
      "responsible": "S26686",
      "servername": "sv00812"
    },
    {
      "applier": "S26686",
      "id": 813,
      "owner": "T8973",
      "purpose": "Worker Core",
      "responsible": "S26686",
      "servername": "sv00813"
    },
    {
      "applier": "S26686",
      "id": 814,
      "owner": "T8973",
      "purpose": "Delivery Controller - Site Marl",
      "responsible": "S26686",
      "servername": "sv00814"
    },
    {
      "applier": "S26686",
      "id": 815,
      "owner": "T8973",
      "purpose": "Delivery Controller - Site Antwerpen",
      "responsible": "S26686",
      "servername": "sv00815"
    },
    {
      "applier": "S26686",
      "id": 816,
      "owner": "T8973",
      "purpose": "Delivery Controller - Site Darmstadt",
      "responsible": "S26686",
      "servername": "sv00816"
    },
    {
      "applier": "Y5011",
      "id": 817,
      "owner": "T8973",
      "purpose": "Worker Core",
      "responsible": "Y5011",
      "servername": "sv00817"
    },
    {
      "applier": "R21409",
      "id": 818,
      "owner": "T8973",
      "purpose": "Delivery Controller - Site Wesseling",
      "responsible": "R21409",
      "servername": "sv00818"
    },
    {
      "applier": "R21409",
      "id": 819,
      "owner": "T8973",
      "purpose": "Delivery Controller - Site Essen Campus",
      "responsible": "R21409",
      "servername": "sv00819"
    },
    {
      "applier": "Y5011",
      "id": 820,
      "owner": "T8973 ",
      "purpose": "Worker Core",
      "responsible": "Y5011",
      "servername": "sv00820"
    },
    {
      "applier": "Y5011",
      "id": 821,
      "owner": "T8973",
      "purpose": "Delivery Controller - Site Rheinfelden",
      "responsible": "Y5011",
      "servername": "sv00821"
    },
    {
      "applier": "Y5011",
      "id": 822,
      "owner": "T8973",
      "purpose": "Worker Core",
      "responsible": "Y5011",
      "servername": "sv00822"
    },
    {
      "applier": "Y5011",
      "id": 823,
      "owner": "T8973 ",
      "purpose": "Worker Core",
      "responsible": "Y5011",
      "servername": "sv00823"
    },
    {
      "applier": "Y5011",
      "id": 824,
      "owner": "T8973",
      "purpose": "Delivery Controller - Site Hanau-Wolfgang",
      "responsible": "Y5011",
      "servername": "sv00824"
    },
    {
      "applier": "R21409",
      "id": 825,
      "owner": "T8973",
      "purpose": "Delivery Controller - Site Essen Goldschmidt",
      "responsible": "R21409",
      "servername": "sv00825"
    },
    {
      "applier": "R21409",
      "id": 826,
      "owner": "T8973",
      "purpose": "Delivery Controller - Site Krefeld",
      "responsible": "R21409",
      "servername": "sv00826"
    },
    {
      "applier": "T15463",
      "id": 827,
      "owner": "C15512",
      "purpose": "Server for isolated domain",
      "responsible": "T15463",
      "servername": "sv00827"
    },
    {
      "applier": "T15463",
      "id": 828,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "T15463",
      "servername": "sv00828"
    },
    {
      "applier": "Y5011",
      "id": 829,
      "owner": "B13074",
      "purpose": "operation",
      "responsible": "Y5011",
      "servername": "sv00829"
    },
    {
      "applier": "S26686",
      "id": 830,
      "owner": "M26814",
      "purpose": "RFT00492170",
      "responsible": "S26686",
      "servername": "sv00830"
    },
    {
      "applier": "S26620",
      "id": 831,
      "owner": "L0067",
      "purpose": "uMCDB Server",
      "responsible": "S26620",
      "servername": "sv00831"
    },
    {
      "applier": "S26686",
      "id": 832,
      "owner": "L0067",
      "purpose": "Embedded uCMDB",
      "responsible": "S26686",
      "servername": "sv00832"
    },
    {
      "applier": "T15463",
      "id": 833,
      "owner": "G12598",
      "purpose": "Windows Server for Oracle databases",
      "responsible": "T15463",
      "servername": "sv00833"
    },
    {
      "applier": "T15463",
      "id": 834,
      "owner": "G12598",
      "purpose": "Windows Server for Oracle databases",
      "responsible": "T15463",
      "servername": "sv00834"
    },
    {
      "applier": "T15463",
      "id": 835,
      "owner": "G12598",
      "purpose": "Windows Server for Oracle databases",
      "responsible": "T15463",
      "servername": "sv00835"
    },
    {
      "applier": "T15463",
      "id": 836,
      "owner": "G12598",
      "purpose": "Windows Server for Oracle databases",
      "responsible": "T15463",
      "servername": "sv00836"
    },
    {
      "applier": "T15463",
      "id": 837,
      "owner": "G12598",
      "purpose": "Windows Server for Oracle databases",
      "responsible": "T15463",
      "servername": "sv00837"
    },
    {
      "applier": "T15463",
      "id": 838,
      "owner": "G12598",
      "purpose": "Windows Server for Oracle databases",
      "responsible": "T15463",
      "servername": "sv00838"
    },
    {
      "applier": "C0371",
      "id": 839,
      "owner": "B0163",
      "purpose": "OpenText Archiv Server",
      "responsible": "C0371",
      "servername": "sv00839"
    },
    {
      "applier": "J0649",
      "id": 840,
      "owner": "J0649",
      "purpose": "File Server IP Camera",
      "responsible": "J0649",
      "servername": "sv00840"
    },
    {
      "applier": "S26620",
      "id": 841,
      "owner": "M3180",
      "purpose": "Messdas Server",
      "responsible": "S26620",
      "servername": "sv00841"
    },
    {
      "applier": "S26620",
      "id": 842,
      "owner": "B1500",
      "purpose": "PoC (CA PM)",
      "responsible": "S26620",
      "servername": "sv00842"
    },
    {
      "applier": "S26620",
      "id": 843,
      "owner": "B1500",
      "purpose": "PoC (CA PM)",
      "responsible": "S26620",
      "servername": "sv00843"
    },
    {
      "applier": "B13085",
      "id": 844,
      "owner": "R0418",
      "purpose": "Server for PIMS LDF",
      "responsible": "B13085",
      "servername": "sv00844"
    },
    {
      "applier": "B13085",
      "id": 845,
      "owner": "G12598",
      "purpose": "Pilot Installation for Microsoft SCOM (Monitoring)",
      "responsible": "B13085",
      "servername": "sv00845"
    },
    {
      "applier": "J19922",
      "id": 846,
      "owner": "D0106",
      "purpose": "TSM",
      "responsible": "J19922",
      "servername": "sv00846"
    },
    {
      "applier": "Y5011",
      "id": 847,
      "owner": "W11165",
      "purpose": "execute KNIME workflows",
      "responsible": "Y5011",
      "servername": "sv00847"
    },
    {
      "applier": "C0371",
      "id": 848,
      "owner": "C11323",
      "purpose": "Saperion/PharmSchul Dev",
      "responsible": "C0371",
      "servername": "sv00848"
    },
    {
      "applier": "C0371",
      "id": 849,
      "owner": "C11323",
      "purpose": "Saperion/PharmSchul Produktiv",
      "responsible": "C0371",
      "servername": "sv00849"
    },
    {
      "applier": "S18344",
      "id": 850,
      "owner": "M0770",
      "purpose": "Empower Application Server Prod",
      "responsible": "S18344",
      "servername": "sv00850"
    },
    {
      "applier": "S18344",
      "id": 851,
      "owner": "M0770",
      "purpose": "Empower Application Server Dev",
      "responsible": "S18344",
      "servername": "sv00851"
    },
    {
      "applier": "S18344",
      "id": 852,
      "owner": "M0770",
      "purpose": "special Apps Terminal Server Empower Prod",
      "responsible": "S18344",
      "servername": "sv00852"
    },
    {
      "applier": "S18344",
      "id": 853,
      "owner": "M0770",
      "purpose": "special Apps Terminal Server Empower Prod",
      "responsible": "S18344",
      "servername": "sv00853"
    },
    {
      "applier": "S18344",
      "id": 854,
      "owner": "M0770",
      "purpose": "special Apps Terminal Server Empower Prod",
      "responsible": "S18344",
      "servername": "sv00854"
    },
    {
      "applier": "S18344",
      "id": 855,
      "owner": "M0770",
      "purpose": "pecial Apps Terminal Server Empower Dev",
      "responsible": "S18344",
      "servername": "sv00855"
    },
    {
      "applier": "S26686",
      "id": 856,
      "owner": "B1500",
      "purpose": "OVA File Installation",
      "responsible": "S26686",
      "servername": "sv00856"
    },
    {
      "applier": "A0423",
      "id": 857,
      "owner": "D1332",
      "purpose": "Ironport Reporting System",
      "responsible": "A0423",
      "servername": "sv00857"
    },
    {
      "applier": "S26620",
      "id": 858,
      "owner": "S20376",
      "purpose": "EBID PROD (WAS-5500)",
      "responsible": "S26620",
      "servername": "sv00858"
    },
    {
      "applier": "S26620",
      "id": 859,
      "owner": "S20376",
      "purpose": "EBID QA (WAS-5500)",
      "responsible": "S26620",
      "servername": "sv00859"
    },
    {
      "applier": "S13571",
      "id": 860,
      "owner": "S13571",
      "purpose": "vSphere Integrated Containers Appliance",
      "responsible": "S13571",
      "servername": "sv00860"
    },
    {
      "applier": "T15463",
      "id": 861,
      "owner": "T15463",
      "purpose": " CyberArk PSM Test Server",
      "responsible": "T15463",
      "servername": "sv00861"
    },
    {
      "applier": "R19376",
      "id": 862,
      "owner": "C15512",
      "purpose": "king.dom DC",
      "responsible": "R19376",
      "servername": "sv00862"
    },
    {
      "applier": "Y5011",
      "id": 863,
      "owner": "M36066",
      "purpose": "Acronis Storage Node Hanau",
      "responsible": "Y5011",
      "servername": "sv00863"
    },
    {
      "applier": "Y5011",
      "id": 864,
      "owner": "D0106",
      "purpose": "SP-Server (ab 7.1.7 ) (MALSP01)",
      "responsible": "Y5011",
      "servername": "sv00864"
    },
    {
      "applier": "S26686",
      "id": 865,
      "owner": "B6833",
      "purpose": "RFT00511566",
      "responsible": "S26686",
      "servername": "sv00865"
    },
    {
      "applier": "Y5011",
      "id": 866,
      "owner": "M23055",
      "purpose": "Application server (production system)",
      "responsible": "Y5011",
      "servername": "sv00866"
    },
    {
      "applier": "S26620",
      "id": 867,
      "owner": "K17867",
      "purpose": "SQL Server",
      "responsible": "S26620",
      "servername": "sv00867"
    },
    {
      "applier": "R21409",
      "id": 868,
      "owner": "K17867",
      "purpose": "Project Server for Infosys",
      "responsible": "R21409",
      "servername": "sv00868"
    },
    {
      "applier": "S26686",
      "id": 869,
      "owner": "B6833",
      "purpose": "WAS-2400 WebViewer Prod",
      "responsible": "S26686",
      "servername": "sv00869"
    },
    {
      "applier": "S26686",
      "id": 870,
      "owner": "B6833",
      "purpose": "WAS-2400 WebViewer QA",
      "responsible": "S26686",
      "servername": "sv00870"
    },
    {
      "applier": "Y5011",
      "id": 871,
      "owner": "D0106",
      "purpose": "SP-Server (ab 7.1.7 )",
      "responsible": "Y5011",
      "servername": "sv00871"
    },
    {
      "applier": "Y5011",
      "id": 872,
      "owner": "D0106",
      "purpose": "SP-Server (ab 7.1.7 ) ",
      "responsible": "Y5011",
      "servername": "sv00872"
    },
    {
      "applier": "S26686",
      "id": 873,
      "owner": "O0371",
      "purpose": "RFT00515555",
      "responsible": "S26686",
      "servername": "sv00873"
    },
    {
      "applier": "S26620",
      "id": 874,
      "owner": "B6833",
      "purpose": "Evonik Redirector QA",
      "responsible": "S26620",
      "servername": "sv00874"
    },
    {
      "applier": "S26620",
      "id": 875,
      "owner": "B6833",
      "purpose": "Evonik Redirector QA",
      "responsible": "S26620",
      "servername": "sv00875"
    },
    {
      "applier": "S26686",
      "id": 876,
      "owner": "S20376",
      "purpose": "Application Splunk",
      "responsible": "S26686",
      "servername": "sv00876"
    },
    {
      "applier": "R19376",
      "id": 877,
      "owner": "J27138",
      "purpose": "ARGIS Server",
      "responsible": "R19376",
      "servername": "sv00877"
    },
    {
      "applier": "S26620",
      "id": 878,
      "owner": "F7813",
      "purpose": "CASB Server",
      "responsible": "S26620",
      "servername": "sv00878"
    },
    {
      "applier": "J0649",
      "id": 879,
      "owner": "J0649",
      "purpose": "Fileserver 1 DC2016",
      "responsible": "J0649",
      "servername": "sv00879"
    },
    {
      "applier": "J0649",
      "id": 880,
      "owner": "J0649",
      "purpose": "Fileserver 2 DC2016",
      "responsible": "J0649",
      "servername": "sv00880"
    },
    {
      "applier": "S26620",
      "id": 881,
      "owner": "D0106",
      "purpose": "SP-Proxy-Server",
      "responsible": "S26620",
      "servername": "sv00881"
    },
    {
      "applier": "S26620",
      "id": 882,
      "owner": "J0649",
      "purpose": " Fileserver",
      "responsible": "S26620",
      "servername": "sv00882"
    },
    {
      "applier": "S26620",
      "id": 883,
      "owner": "J0649",
      "purpose": " Fileserver",
      "responsible": "S26620",
      "servername": "sv00883"
    },
    {
      "applier": "S13571",
      "id": 884,
      "owner": "S13571",
      "purpose": "Storage Server K\u00c3\u00bcnsebeck",
      "responsible": "S13571",
      "servername": "sv00884"
    },
    {
      "applier": "S13571",
      "id": 885,
      "owner": "S13571",
      "purpose": "USB Dongle Server K\u00c3\u00bcnsebeck",
      "responsible": "S13571",
      "servername": "sv00885"
    },
    {
      "applier": "S13571",
      "id": 886,
      "owner": "S13571",
      "purpose": "Oracle K\u00c3\u00bcnsebeck",
      "responsible": "S13571",
      "servername": "sv00886"
    },
    {
      "applier": "S18344",
      "id": 887,
      "owner": "S13571",
      "purpose": "Veeam Proxy ( Cluster es1hc03clu01)",
      "responsible": "S18344",
      "servername": "sv00887"
    },
    {
      "applier": "T15463",
      "id": 888,
      "owner": "S13571",
      "purpose": "Veeam Proxy Server ",
      "responsible": "T15463",
      "servername": "sv00888"
    },
    {
      "applier": "T15463",
      "id": 889,
      "owner": "S13571",
      "purpose": "Veeam Proxy Server ",
      "responsible": "T15463",
      "servername": "sv00889"
    },
    {
      "applier": "C0371",
      "id": 890,
      "owner": "R4657",
      "purpose": "Tiamo",
      "responsible": "C0371",
      "servername": "sv00890"
    },
    {
      "applier": "S26686",
      "id": 891,
      "owner": "I0378",
      "purpose": "RFT00527224",
      "responsible": "S26686",
      "servername": "sv00891"
    },
    {
      "applier": "S26686",
      "id": 892,
      "owner": "K0563",
      "purpose": "ClickShare presentation",
      "responsible": "S26686",
      "servername": "sv00892"
    },
    {
      "applier": "R19376",
      "id": 893,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "R19376",
      "servername": "sv00893"
    },
    {
      "applier": "S26620",
      "id": 894,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "S26620",
      "servername": "sv00894"
    },
    {
      "applier": "S26620",
      "id": 895,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "S26620",
      "servername": "sv00895"
    },
    {
      "applier": "R19376",
      "id": 896,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "R19376",
      "servername": "sv00896"
    },
    {
      "applier": "Y5011",
      "id": 897,
      "owner": "S0060",
      "purpose": "SP-0500 NOM",
      "responsible": "Y5011",
      "servername": "sv00897"
    },
    {
      "applier": "Y5011",
      "id": 898,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "Y5011",
      "servername": "sv00898"
    },
    {
      "applier": "S26620",
      "id": 899,
      "owner": "K14435",
      "purpose": "RPA technology",
      "responsible": "S26620",
      "servername": "sv00899"
    },
    {
      "applier": "S26620",
      "id": 900,
      "owner": "T16054",
      "purpose": "WAS-5700 Master Control eDMS",
      "responsible": "S26620",
      "servername": "sv00900"
    },
    {
      "applier": "R19376",
      "id": 901,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "R19376",
      "servername": "sv00901"
    },
    {
      "applier": "h17255",
      "id": 902,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "H17255",
      "servername": "sv00902"
    },
    {
      "applier": "h17255",
      "id": 903,
      "owner": "C15511",
      "purpose": "Domain Controller",
      "responsible": "H17255",
      "servername": "sv00903"
    },
    {
      "applier": "h17255",
      "id": 904,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "H17255",
      "servername": "sv00904"
    },
    {
      "applier": "C15512",
      "id": 905,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "C15512",
      "servername": "sv00905"
    },
    {
      "applier": "C15512",
      "id": 906,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "C15512",
      "servername": "sv00906"
    },
    {
      "applier": "C15512",
      "id": 907,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "C15512",
      "servername": "sv00907"
    },
    {
      "applier": "C15512",
      "id": 908,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "C15512",
      "servername": "sv00908"
    },
    {
      "applier": "J0649",
      "id": 909,
      "owner": "D18547",
      "purpose": "VMware Host",
      "responsible": "D18547",
      "servername": "sv00909"
    },
    {
      "applier": "J0649",
      "id": 910,
      "owner": "J0649",
      "purpose": "File Service",
      "responsible": "J0649",
      "servername": "sv00910"
    },
    {
      "applier": "J0649",
      "id": 911,
      "owner": "I4738",
      "purpose": "App Server",
      "responsible": "I4738",
      "servername": "sv00911"
    },
    {
      "applier": "J0649",
      "id": 912,
      "owner": "I4738",
      "purpose": "App Server 2",
      "responsible": "I4738",
      "servername": "sv00912"
    },
    {
      "applier": "J0649",
      "id": 913,
      "owner": "I4738",
      "purpose": "App Server 3",
      "responsible": "I4738",
      "servername": "sv00913"
    },
    {
      "applier": "J0649",
      "id": 914,
      "owner": "I4738",
      "purpose": "App Server 4",
      "responsible": "I4738",
      "servername": "sv00914"
    },
    {
      "applier": "J0649",
      "id": 915,
      "owner": "M23083",
      "purpose": "SCCM Server",
      "responsible": "M23083",
      "servername": "sv00915"
    },
    {
      "applier": "R19376",
      "id": 916,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "R19376",
      "servername": "sv00916"
    },
    {
      "applier": "\\R19376",
      "id": 917,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "R19376",
      "servername": "sv00917"
    },
    {
      "applier": "\\R19376",
      "id": 918,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "R19376",
      "servername": "sv00918"
    },
    {
      "applier": "\\R19376",
      "id": 919,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "R19376",
      "servername": "sv00919"
    },
    {
      "applier": "AD0233",
      "id": 920,
      "owner": "M30705",
      "purpose": "Test Server",
      "responsible": "D18269",
      "servername": "sv00920"
    },
    {
      "applier": "\\R19376",
      "id": 921,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "R19376",
      "servername": "sv00921"
    },
    {
      "applier": "AB0329",
      "id": 922,
      "owner": "C15512",
      "purpose": "Server 2016 Domain Controller  M1003-Site  ",
      "responsible": "D15437",
      "servername": "sv00922"
    },
    {
      "applier": "AB0329",
      "id": 923,
      "owner": "I4738",
      "purpose": "Application server for M-Files ",
      "responsible": "D15437",
      "servername": "sv00923"
    },
    {
      "applier": "\\R19376",
      "id": 924,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "R19376",
      "servername": "sv00924"
    },
    {
      "applier": "AS0494",
      "id": 925,
      "owner": "S0295",
      "purpose": "Cisco Industrial Network Director",
      "responsible": "S26620",
      "servername": "sv00925"
    },
    {
      "applier": "AS0494",
      "id": 926,
      "owner": "M23055",
      "purpose": "Application Server",
      "responsible": "S26620",
      "servername": "sv00926"
    },
    {
      "applier": "AY0017",
      "id": 927,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "D15437",
      "servername": "sv00927"
    },
    {
      "applier": "AS0500",
      "id": 928,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "D18547",
      "servername": "sv00928"
    },
    {
      "applier": "AS0500",
      "id": 929,
      "owner": "F1768",
      "purpose": "RFT00530525",
      "responsible": "D18547",
      "servername": "sv00929"
    },
    {
      "applier": "AS0500",
      "id": 930,
      "owner": "F1768",
      "purpose": "RFT00530525",
      "responsible": "D18547",
      "servername": "sv00930"
    },
    {
      "applier": "AS0500",
      "id": 931,
      "owner": "F1768",
      "purpose": "RFT00530525",
      "responsible": "D18547",
      "servername": "sv00931"
    },
    {
      "applier": "AS0500",
      "id": 932,
      "owner": "F1768",
      "purpose": "RFT00530525",
      "responsible": "D18547",
      "servername": "sv00932"
    },
    {
      "applier": "AS0500",
      "id": 933,
      "owner": "F1768",
      "purpose": "RFT00530525",
      "responsible": "D18547",
      "servername": "sv00933"
    },
    {
      "applier": "AY0017",
      "id": 934,
      "owner": "J0649",
      "purpose": "RFT00533746",
      "responsible": "A0423",
      "servername": "sv00934"
    },
    {
      "applier": "AR0279",
      "id": 935,
      "owner": "C15512",
      "purpose": "PowerBroker Server ",
      "responsible": "D18547",
      "servername": "sv00935"
    },
    {
      "applier": "AR0279",
      "id": 936,
      "owner": "C15512",
      "purpose": "PowerBroker Server",
      "responsible": "D18547",
      "servername": "sv00936"
    },
    {
      "applier": "AT0403",
      "id": 937,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "D18547",
      "servername": "sv00937"
    },
    {
      "applier": "AR0279",
      "id": 938,
      "owner": "B6833",
      "purpose": "Evonik Redirector Production",
      "responsible": "F1028",
      "servername": "sv00938"
    },
    {
      "applier": "AR0279",
      "id": 939,
      "owner": "B6833",
      "purpose": "Evonik Redirector Production",
      "responsible": "F1028",
      "servername": "sv00939"
    },
    {
      "applier": "\\R19376",
      "id": 940,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "R19376",
      "servername": "sv00940"
    },
    {
      "applier": "\\R19376",
      "id": 941,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "R19376",
      "servername": "sv00941"
    },
    {
      "applier": "AT0403",
      "id": 942,
      "owner": "T16054",
      "purpose": "Domain Controller",
      "responsible": "D15437",
      "servername": "sv00942"
    },
    {
      "applier": "AY0017",
      "id": 943,
      "owner": "T16054",
      "purpose": "WAS-5700 eDMS QA",
      "responsible": "A0423",
      "servername": "sv00943"
    },
    {
      "applier": "AT0403",
      "id": 944,
      "owner": "T16054",
      "purpose": "WAS-5700 eDMS QA",
      "responsible": "A0423",
      "servername": "sv00944"
    },
    {
      "applier": "99",
      "id": 945,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "N5199",
      "servername": "sv00945"
    },
    {
      "applier": "AT0403",
      "id": 946,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "D15437",
      "servername": "sv00946"
    },
    {
      "applier": "99",
      "id": 947,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "N5199",
      "servername": "sv00947"
    },
    {
      "applier": "99",
      "id": 948,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "N5199",
      "servername": "sv00948"
    },
    {
      "applier": "AB0329",
      "id": 949,
      "owner": "T16054",
      "purpose": "WAS-5700 eDMS Prod",
      "responsible": "O0067",
      "servername": "sv00949"
    },
    {
      "applier": "D7982",
      "id": 950,
      "owner": "R15590",
      "purpose": "TrendMiner",
      "responsible": "D7982",
      "servername": "sv00950"
    },
    {
      "applier": "A0423",
      "id": 951,
      "owner": "M6364",
      "purpose": "Smart Software Manager Client",
      "responsible": "A0423",
      "servername": "sv00951"
    },
    {
      "applier": "A0423",
      "id": 952,
      "owner": "M6364",
      "purpose": "Smart Net Total Care",
      "responsible": "A0423",
      "servername": "sv00952"
    },
    {
      "applier": "\\R19376",
      "id": 953,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "R19376",
      "servername": "sv00953"
    },
    {
      "applier": "\\R19376",
      "id": 954,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "R19376",
      "servername": "sv00954"
    },
    {
      "applier": "255",
      "id": 955,
      "owner": "P12443",
      "purpose": "PHAST Licencing Server",
      "responsible": "H17255",
      "servername": "sv00955"
    },
    {
      "applier": "AS0494",
      "id": 956,
      "owner": "M23816",
      "purpose": "SP-0500 NOM",
      "responsible": "S26620",
      "servername": "sv00956"
    },
    {
      "applier": "AS0494",
      "id": 957,
      "owner": "M23816",
      "purpose": "SP-0500 NOM",
      "responsible": "S26620",
      "servername": "sv00957"
    },
    {
      "applier": "33",
      "id": 958,
      "owner": "C0578",
      "purpose": "BIS Server",
      "responsible": "C0578",
      "servername": "sv00958"
    },
    {
      "applier": "33",
      "id": 959,
      "owner": "H15639",
      "purpose": "Database Server, production system eVIS",
      "responsible": "H15639",
      "servername": "sv00959"
    },
    {
      "applier": "33",
      "id": 960,
      "owner": "H15639",
      "purpose": "Application Server, production system eVIS",
      "responsible": "H15639",
      "servername": "sv00960"
    },
    {
      "applier": "33",
      "id": 961,
      "owner": "T0715",
      "purpose": "PIMS Server",
      "responsible": "T0715",
      "servername": "sv00961"
    },
    {
      "applier": "\\R19376",
      "id": 962,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "R19376",
      "servername": "sv00962"
    },
    {
      "applier": "\\R19376",
      "id": 963,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "R19376",
      "servername": "sv00963"
    },
    {
      "applier": "\\R19376",
      "id": 964,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "R19376",
      "servername": "sv00964"
    },
    {
      "applier": "\\R19376",
      "id": 965,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "R19376",
      "servername": "sv00965"
    },
    {
      "applier": "382",
      "id": 966,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "C15512",
      "servername": "sv00966"
    },
    {
      "applier": "AB0329",
      "id": 967,
      "owner": "C15512",
      "purpose": "Server 2016 Domain Controller M0134 Site",
      "responsible": "A0423",
      "servername": "sv00967"
    },
    {
      "applier": "AB0329",
      "id": 968,
      "owner": "C15512",
      "purpose": "Server 2016 Domain Controller \u00e2\u20ac\u201c M0134-Site",
      "responsible": "A0423",
      "servername": "sv00968"
    },
    {
      "applier": "AB0329",
      "id": 969,
      "owner": "C15512",
      "purpose": "Server 2016 Domain Controller \u00e2\u20ac\u201c M0174-Site ",
      "responsible": "A0423",
      "servername": "sv00969"
    },
    {
      "applier": "AB0329",
      "id": 970,
      "owner": "C15512",
      "purpose": "Server 2016 Domain Controller \u00e2\u20ac\u201c M0174-Site ",
      "responsible": "A0423",
      "servername": "sv00970"
    },
    {
      "applier": "382",
      "id": 971,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "C15512",
      "servername": "sv00971"
    },
    {
      "applier": "AS0494",
      "id": 972,
      "owner": "L8858",
      "purpose": "Foundation Server",
      "responsible": "S26620",
      "servername": "sv00972"
    },
    {
      "applier": "AS0494",
      "id": 973,
      "owner": "L8858",
      "purpose": "LIMS DEV",
      "responsible": "S26620",
      "servername": "sv00973"
    },
    {
      "applier": "382",
      "id": 974,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "C15512",
      "servername": "sv00974"
    },
    {
      "applier": "382",
      "id": 975,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "C15512",
      "servername": "sv00975"
    },
    {
      "applier": "AD0233",
      "id": 976,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "C15512",
      "servername": "sv00976"
    },
    {
      "applier": "AR0279",
      "id": 977,
      "owner": "T16054",
      "purpose": "WAS-5600 Idea2Poduct",
      "responsible": "D18547",
      "servername": "sv00977"
    },
    {
      "applier": "\\M32214",
      "id": 978,
      "owner": "M32214",
      "purpose": "TSM Backup Server ",
      "responsible": "M32214",
      "servername": "sv00978"
    },
    {
      "applier": "382",
      "id": 979,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "C15512",
      "servername": "sv00979"
    },
    {
      "applier": "382",
      "id": 980,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "C15512",
      "servername": "sv00980"
    },
    {
      "applier": "AY0017",
      "id": 981,
      "owner": "F8735",
      "purpose": "Jumphosts for the ISAM Server",
      "responsible": "D18547",
      "servername": "sv00981"
    },
    {
      "applier": "99",
      "id": 982,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "N5199",
      "servername": "sv00982"
    },
    {
      "applier": "AS0500",
      "id": 983,
      "owner": "T16054",
      "purpose": "WEB_GENERIC_QA",
      "responsible": "D18547",
      "servername": "sv00983"
    },
    {
      "applier": "AS0500",
      "id": 984,
      "owner": "T16054",
      "purpose": "WEB_GENERIC_PROD",
      "responsible": "D18547",
      "servername": "sv00984"
    },
    {
      "applier": "AS0500",
      "id": 985,
      "owner": "T16054",
      "purpose": "RFT00556904",
      "responsible": "D18547",
      "servername": "sv00985"
    },
    {
      "applier": "AT0403",
      "id": 986,
      "owner": "F1768",
      "purpose": "Application",
      "responsible": "C0371",
      "servername": "sv00986"
    },
    {
      "applier": "AT0403",
      "id": 987,
      "owner": "F1768",
      "purpose": "Gxp Application Server",
      "responsible": "C0371",
      "servername": "sv00987"
    },
    {
      "applier": "AT0403",
      "id": 988,
      "owner": "F1768",
      "purpose": "Application",
      "responsible": "C0371",
      "servername": "sv00988"
    },
    {
      "applier": "AT0403",
      "id": 989,
      "owner": "F1768",
      "purpose": "Application",
      "responsible": "C0371",
      "servername": "sv00989"
    },
    {
      "applier": "AS0500",
      "id": 990,
      "owner": "C15512",
      "purpose": " Domain Controller ",
      "responsible": "D18547",
      "servername": "sv00990"
    },
    {
      "applier": "AT0403",
      "id": 991,
      "owner": "F1768",
      "purpose": "Application",
      "responsible": "C0371",
      "servername": "sv00991"
    },
    {
      "applier": "AT0403",
      "id": 992,
      "owner": "F1768",
      "purpose": "Application",
      "responsible": "C0371",
      "servername": "sv00992"
    },
    {
      "applier": "AT0403",
      "id": 993,
      "owner": "F1768",
      "purpose": "Application",
      "responsible": "C0371",
      "servername": "sv00993"
    },
    {
      "applier": "AT0403",
      "id": 994,
      "owner": "F1768",
      "purpose": "Application",
      "responsible": "C0371",
      "servername": "sv00994"
    },
    {
      "applier": "AT0403",
      "id": 995,
      "owner": "F1768",
      "purpose": "Application",
      "responsible": "C0371",
      "servername": "sv00995"
    },
    {
      "applier": "AT0403",
      "id": 996,
      "owner": "F1768",
      "purpose": "Application",
      "responsible": "C0371",
      "servername": "sv00996"
    },
    {
      "applier": "AT0403",
      "id": 997,
      "owner": "F1768",
      "purpose": "Application",
      "responsible": "D15437",
      "servername": "sv00997"
    },
    {
      "applier": "AT0403",
      "id": 998,
      "owner": "F1768",
      "purpose": "Application",
      "responsible": "D15437",
      "servername": "sv00998"
    },
    {
      "applier": "AT0403",
      "id": 999,
      "owner": "F1768",
      "purpose": "Application",
      "responsible": "D15437",
      "servername": "sv00999"
    },
    {
      "applier": "AT0403",
      "id": 1000,
      "owner": "F1768",
      "purpose": "Application",
      "responsible": "D15437",
      "servername": "sv01000"
    },
    {
      "applier": "AT0403",
      "id": 1001,
      "owner": "F1768",
      "purpose": "Application",
      "responsible": "D15437",
      "servername": "sv01001"
    },
    {
      "applier": "G12866",
      "id": 1002,
      "owner": "S18344",
      "purpose": "QA Server Firmware/Driver Rollout",
      "responsible": "G12866",
      "servername": "sv01002"
    },
    {
      "applier": "G12866",
      "id": 1003,
      "owner": "S18344",
      "purpose": "QA Server Firmware/Driver Rollout",
      "responsible": "G12866",
      "servername": "sv01003"
    },
    {
      "applier": "G12866",
      "id": 1004,
      "owner": "S18344",
      "purpose": "QA Server Firmware/Driver Rollout",
      "responsible": "G12866",
      "servername": "sv01004"
    },
    {
      "applier": "G12866",
      "id": 1005,
      "owner": "S18344",
      "purpose": "QA Server Firmware/Driver Rollout",
      "responsible": "G12866",
      "servername": "sv01005"
    },
    {
      "applier": "G12866",
      "id": 1006,
      "owner": "S18344",
      "purpose": "QA Server Firmware/Driver Rollout",
      "responsible": "G12866",
      "servername": "sv01006"
    },
    {
      "applier": "G12866",
      "id": 1007,
      "owner": "S18344",
      "purpose": "QA Server Firmware/Driver Rollout",
      "responsible": "G12866",
      "servername": "sv01007"
    },
    {
      "applier": "AS0494",
      "id": 1008,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "S26620",
      "servername": "sv01008"
    },
    {
      "applier": "79",
      "id": 1009,
      "owner": "T16054",
      "purpose": "WAS-5700 eDMS Prod",
      "responsible": "D18547",
      "servername": "sv01009"
    },
    {
      "applier": "AY0017",
      "id": 1010,
      "owner": "S25180",
      "purpose": "K2 environment",
      "responsible": "D18547",
      "servername": "sv01010"
    },
    {
      "applier": "A0423",
      "id": 1011,
      "owner": "K680010",
      "purpose": "QA NAAF Server",
      "responsible": "A0423",
      "servername": "sv01011"
    },
    {
      "applier": "A0423",
      "id": 1012,
      "owner": "K680010",
      "purpose": "QA NAAF Server",
      "responsible": "A0423",
      "servername": "sv01012"
    },
    {
      "applier": "A0423",
      "id": 1013,
      "owner": "K680010",
      "purpose": " DEV NAAF Server",
      "responsible": "A0423",
      "servername": "sv01013"
    },
    {
      "applier": "A0423",
      "id": 1014,
      "owner": "K680010",
      "purpose": "DEV NAAF Server",
      "responsible": "A0423",
      "servername": "sv01014"
    },
    {
      "applier": "A0423",
      "id": 1015,
      "owner": "K680010",
      "purpose": "PROD NAAF Server",
      "responsible": "A0423",
      "servername": "sv01015"
    },
    {
      "applier": "A0423",
      "id": 1016,
      "owner": "K680010",
      "purpose": "PROD NAAF Server",
      "responsible": "A0423",
      "servername": "sv01016"
    },
    {
      "applier": "S18344",
      "id": 1017,
      "owner": "S18344",
      "purpose": "MS Orchestrator Runbookserver SPP_Deployment QA",
      "responsible": "S18344",
      "servername": "sv01017"
    },
    {
      "applier": "AS0494",
      "id": 1018,
      "owner": "T8973",
      "purpose": "Special-App ASP Server",
      "responsible": "S26620",
      "servername": "sv01018"
    },
    {
      "applier": "AS0494",
      "id": 1019,
      "owner": "T8973",
      "purpose": "Special-App ASP Server",
      "responsible": "S26620",
      "servername": "sv01019"
    },
    {
      "applier": "AS0494",
      "id": 1020,
      "owner": "T8973",
      "purpose": "Special-App ASP Server",
      "responsible": "S26620",
      "servername": "sv01020"
    },
    {
      "applier": "AS0494",
      "id": 1021,
      "owner": "T8973",
      "purpose": "Special-App ASP Server",
      "responsible": "S26620",
      "servername": "sv01021"
    },
    {
      "applier": "AS0494",
      "id": 1022,
      "owner": "T8973",
      "purpose": "Special-App ASP Server",
      "responsible": "S26620",
      "servername": "sv01022"
    },
    {
      "applier": "AS0494",
      "id": 1023,
      "owner": "T8973",
      "purpose": " Special-App ASP Server",
      "responsible": "S26620",
      "servername": "sv01023"
    },
    {
      "applier": "J19922",
      "id": 1024,
      "owner": "J19922",
      "purpose": "TSM ME5",
      "responsible": "J19922",
      "servername": "sv01024"
    },
    {
      "applier": "J19922",
      "id": 1025,
      "owner": "J19922",
      "purpose": "ME6 ESX1",
      "responsible": "J19922",
      "servername": "sv01025"
    },
    {
      "applier": "J19922",
      "id": 1026,
      "owner": "J19922",
      "purpose": "ME6 ESX2",
      "responsible": "J19922",
      "servername": "sv01026"
    },
    {
      "applier": "J19922",
      "id": 1027,
      "owner": "J19922",
      "purpose": "ME6 ESX3",
      "responsible": "J19922",
      "servername": "sv01027"
    },
    {
      "applier": "J19922",
      "id": 1028,
      "owner": "J19922",
      "purpose": "ME6 ESX4",
      "responsible": "J19922",
      "servername": "sv01028"
    },
    {
      "applier": "AS0500",
      "id": 1029,
      "owner": "L8858",
      "purpose": "RFT00553465",
      "responsible": "D18547",
      "servername": "sv01029"
    },
    {
      "applier": "AS0500",
      "id": 1030,
      "owner": "T16054",
      "purpose": " WAS-5600 Idea2Poduct",
      "responsible": "D18547",
      "servername": "sv01030"
    },
    {
      "applier": "AY0017",
      "id": 1031,
      "owner": "T16054",
      "purpose": "WAS-5600 Idea2Poduct",
      "responsible": "D15437",
      "servername": "sv01031"
    },
    {
      "applier": "D7982",
      "id": 1032,
      "owner": "T16054",
      "purpose": "WAS-5600 Idea2Poduct",
      "responsible": "D7982",
      "servername": "sv01032"
    },
    {
      "applier": "\\R19376",
      "id": 1033,
      "owner": "R19376",
      "purpose": "Jump Server",
      "responsible": "R19376",
      "servername": "sv01033"
    },
    {
      "applier": "AY0017",
      "id": 1034,
      "owner": "C15512",
      "purpose": "Application Server",
      "responsible": "D15437",
      "servername": "sv01034"
    },
    {
      "applier": "AR0279",
      "id": 1035,
      "owner": "M23055",
      "purpose": "neue Webserver",
      "responsible": "D18547",
      "servername": "sv01035"
    },
    {
      "applier": "514",
      "id": 1036,
      "owner": "S19749",
      "purpose": "ASP Special Citrix Server",
      "responsible": "S19749",
      "servername": "sv01036"
    },
    {
      "applier": "514",
      "id": 1037,
      "owner": "S19749",
      "purpose": "ASP Special Citrix Server",
      "responsible": "S19749",
      "servername": "sv01037"
    },
    {
      "applier": "AY0017",
      "id": 1038,
      "owner": "L8858",
      "purpose": "Foundation Server",
      "responsible": "G12866",
      "servername": "sv01038"
    },
    {
      "applier": "D15437",
      "id": 1039,
      "owner": "A0751",
      "purpose": "Notes Mail Server",
      "responsible": "D15437",
      "servername": "sv01039"
    },
    {
      "applier": "D15437",
      "id": 1040,
      "owner": "A0751",
      "purpose": "Notes Mail Server Archiv",
      "responsible": "D15437",
      "servername": "sv01040"
    },
    {
      "applier": "94",
      "id": 1041,
      "owner": "T16054",
      "purpose": "WAS-5600 Idea2PoductStage",
      "responsible": "S26620",
      "servername": "sv01041"
    },
    {
      "applier": "GA2624",
      "id": 1042,
      "owner": "C10477",
      "purpose": "Test Productive Environment",
      "responsible": "C10477",
      "servername": "sv01042"
    },
    {
      "applier": "94",
      "id": 1043,
      "owner": "B0246",
      "purpose": "WWI/Expert server Prod 1",
      "responsible": "S26620",
      "servername": "sv01043"
    },
    {
      "applier": "94",
      "id": 1044,
      "owner": "B0246",
      "purpose": "WWI/Expert server Prod 2",
      "responsible": "S26620",
      "servername": "sv01044"
    },
    {
      "applier": "AD0233",
      "id": 1045,
      "owner": "O1854",
      "purpose": "ASP eDesk Core Server",
      "responsible": "O1854",
      "servername": "sv01045"
    },
    {
      "applier": "AD0233",
      "id": 1046,
      "owner": "O1854",
      "purpose": "ASP eDesk Core Server",
      "responsible": "O1854",
      "servername": "sv01046"
    },
    {
      "applier": "AD0233",
      "id": 1047,
      "owner": "O1854",
      "purpose": "ASP eDesk Core Server",
      "responsible": "O1854",
      "servername": "sv01047"
    },
    {
      "applier": "AS0500",
      "id": 1048,
      "owner": "K1583",
      "purpose": "RFT00579587",
      "responsible": "D18547",
      "servername": "sv01048"
    },
    {
      "applier": "AD0233",
      "id": 1049,
      "owner": "O1854",
      "purpose": "ASP eDesk Core Server",
      "responsible": "O1854",
      "servername": "sv01049"
    },
    {
      "applier": "AD0233",
      "id": 1050,
      "owner": "O1854",
      "purpose": "ASP eDesk Core Server",
      "responsible": "O1854",
      "servername": "sv01050"
    },
    {
      "applier": "AD0233",
      "id": 1051,
      "owner": "O1854",
      "purpose": "ASP eDesk Core Server",
      "responsible": "O1854",
      "servername": "sv01051"
    },
    {
      "applier": "GA2624",
      "id": 1052,
      "owner": "S18344",
      "purpose": "MS Orchestrator Runbookserver SPP_Deployment APAC",
      "responsible": "S18344",
      "servername": "sv01052"
    },
    {
      "applier": "GA2624",
      "id": 1053,
      "owner": "S18344",
      "purpose": "MS Orchestrator Runbookserver SPP_Deployment APAC",
      "responsible": "S18344",
      "servername": "sv01053"
    },
    {
      "applier": "GA2624",
      "id": 1055,
      "owner": "S18344",
      "purpose": "MS Orchestrator Runbookserver SPP_Deployment APAC",
      "responsible": "S18344",
      "servername": "sv01055"
    },
    {
      "applier": "GA2624",
      "id": 1056,
      "owner": "S18344",
      "purpose": "MS Orchestrator Runbookserver SPP_Deployment AMERICAS",
      "responsible": "S18344",
      "servername": "sv01056"
    },
    {
      "applier": "A1912",
      "id": 1057,
      "owner": "D0106",
      "purpose": "SP-Server (ab 7.1.7 ) (ESRSP01)",
      "responsible": "A1912",
      "servername": "sv01057"
    },
    {
      "applier": "D7982",
      "id": 1058,
      "owner": "D0106",
      "purpose": "Cisco ISP S3260",
      "responsible": "D7982",
      "servername": "sv01058"
    },
    {
      "applier": "AY0017",
      "id": 1059,
      "owner": "C11917",
      "purpose": "ArcSight Connector Server",
      "responsible": "D15437",
      "servername": "sv01059"
    },
    {
      "applier": "A0423",
      "id": 1060,
      "owner": "A0423",
      "purpose": "VMware vSphere Data Protection Appliance 6.1",
      "responsible": "A0423",
      "servername": "sv01060"
    },
    {
      "applier": "AB0329",
      "id": 1061,
      "owner": "M23734",
      "purpose": "OpenText upgrade project",
      "responsible": "A0423",
      "servername": "sv01061"
    },
    {
      "applier": "AB0329",
      "id": 1062,
      "owner": "M23734",
      "purpose": "OpenText upgrade project",
      "responsible": "A0423",
      "servername": "sv01062"
    },
    {
      "applier": "AB0329",
      "id": 1063,
      "owner": "M23734",
      "purpose": "OpenText upgrade project",
      "responsible": "A0423",
      "servername": "sv01063"
    },
    {
      "applier": "GA2624",
      "id": 1064,
      "owner": "C10477",
      "purpose": "DEV Orchestration Server",
      "responsible": "C10477",
      "servername": "sv01064"
    },
    {
      "applier": "AS0500",
      "id": 1065,
      "owner": "C14559",
      "purpose": "License Control for SAP",
      "responsible": "D18547",
      "servername": "sv01065"
    },
    {
      "applier": "C0371",
      "id": 1066,
      "owner": "M36066",
      "purpose": "Acronis",
      "responsible": "C0371",
      "servername": "sv01066"
    },
    {
      "applier": "AR0279",
      "id": 1067,
      "owner": "C1385",
      "purpose": "Application server",
      "responsible": "D18547",
      "servername": "sv01067"
    },
    {
      "applier": "AB0329",
      "id": 1068,
      "owner": "H1053",
      "purpose": "virtual File Transfer Server (FTP, SFTP) on site",
      "responsible": "A0423",
      "servername": "sv01068"
    },
    {
      "applier": "AB0329",
      "id": 1069,
      "owner": "H1053",
      "purpose": "virtual File Transfer Server in a datacenter",
      "responsible": "A0423",
      "servername": "sv01069"
    },
    {
      "applier": "AB0329",
      "id": 1070,
      "owner": "H1053",
      "purpose": "virtual (no Citrix!) Server for remote access ",
      "responsible": "A0423",
      "servername": "sv01070"
    },
    {
      "applier": "AB0329",
      "id": 1071,
      "owner": "H1053",
      "purpose": "virtual (Citrix?) Server for remote access",
      "responsible": "A0423",
      "servername": "sv01071"
    },
    {
      "applier": "GA2624",
      "id": 1072,
      "owner": "S19285",
      "purpose": "Webserver",
      "responsible": "S19285",
      "servername": "sv01072"
    },
    {
      "applier": "GA2624",
      "id": 1073,
      "owner": "S19285",
      "purpose": "MOB Shared Application Server",
      "responsible": "B11210",
      "servername": "sv01073"
    },
    {
      "applier": "\\R19376",
      "id": 1074,
      "owner": "M26165",
      "purpose": "Engineering Dashboard Server",
      "responsible": "R19376",
      "servername": "sv01074"
    },
    {
      "applier": "GA2624",
      "id": 1075,
      "owner": "S19285",
      "purpose": "MOB Shared Application Server",
      "responsible": "B11210",
      "servername": "sv01075"
    },
    {
      "applier": "AS0500",
      "id": 1076,
      "owner": "F1768",
      "purpose": "RFT00594406",
      "responsible": "D18547",
      "servername": "sv01076"
    },
    {
      "applier": "A0423",
      "id": 1077,
      "owner": "A0423",
      "purpose": "VDP Server Darmstadt",
      "responsible": "A0423",
      "servername": "sv01077"
    },
    {
      "applier": "A0423",
      "id": 1078,
      "owner": "A0423",
      "purpose": "VDP Server Darmstadt",
      "responsible": "A0423",
      "servername": "sv01078"
    },
    {
      "applier": "GA2624",
      "id": 1079,
      "owner": "M34002",
      "purpose": "Produktiver Primion Webserver f\u00fcr Marl",
      "responsible": "C10477",
      "servername": "sv01079"
    },
    {
      "applier": "GA2624",
      "id": 1080,
      "owner": "M34002",
      "purpose": "Produktiver Primion Dienstserver f\u00fcr Marl",
      "responsible": "C10477",
      "servername": "sv01080"
    },
    {
      "applier": "GA2624",
      "id": 1081,
      "owner": "M34002",
      "purpose": "Test Primion Web- und Dienstserver f\u00fcr Marl",
      "responsible": "C10477",
      "servername": "sv01081"
    },
    {
      "applier": "GA2624",
      "id": 1082,
      "owner": "M34002",
      "purpose": "Produktiver Primion Web- und Dienstserver f\u00fcr Essen, Herne, Krefeld, Witten, Darmstadt, Steinau",
      "responsible": "C10477",
      "servername": "sv01082"
    },
    {
      "applier": "GA2624",
      "id": 1083,
      "owner": "S19285",
      "purpose": "SQL Server Marl",
      "responsible": "C10477",
      "servername": "sv01083"
    },
    {
      "applier": "GA2624",
      "id": 1084,
      "owner": "S19285",
      "purpose": "SQL Server Marl",
      "responsible": "C10477",
      "servername": "sv01084"
    },
    {
      "applier": "GA2624",
      "id": 1085,
      "owner": "S19285",
      "purpose": "SQL Server Marl",
      "responsible": "C10477",
      "servername": "sv01085"
    },
    {
      "applier": "GA2624",
      "id": 1086,
      "owner": "S19285",
      "purpose": "SQL Server Marl",
      "responsible": "C10477",
      "servername": "sv01086"
    },
    {
      "applier": "AS0494",
      "id": 1087,
      "owner": "M35155",
      "purpose": "POC Process Mining for ITSM",
      "responsible": "S26620",
      "servername": "sv01087"
    },
    {
      "applier": "A0423",
      "id": 1088,
      "owner": "H1456",
      "purpose": "ContactCenterMediaServer",
      "responsible": "A0423",
      "servername": "sv01088"
    },
    {
      "applier": "\\R19376",
      "id": 1089,
      "owner": "K15249",
      "purpose": "Aspen v10 Host",
      "responsible": "R19376",
      "servername": "sv01089"
    },
    {
      "applier": "\\R19376",
      "id": 1090,
      "owner": "E8628",
      "purpose": "ApSEC Application Server",
      "responsible": "R19376",
      "servername": "sv01090"
    },
    {
      "applier": "AS0500",
      "id": 1091,
      "owner": "N5163",
      "purpose": " 9.2 sandbox instances",
      "responsible": "D18547",
      "servername": "sv01091"
    },
    {
      "applier": "AS0500",
      "id": 1092,
      "owner": "T8973",
      "purpose": "RFT00597167",
      "responsible": "D18547",
      "servername": "sv01092"
    },
    {
      "applier": "AS0500",
      "id": 1093,
      "owner": "T8973",
      "purpose": "RFT00597167",
      "responsible": "D18547",
      "servername": "sv01093"
    },
    {
      "applier": "94",
      "id": 1094,
      "owner": "L8858",
      "purpose": "WAS-5800: LIMS - DEV",
      "responsible": "S26620",
      "servername": "sv01094"
    },
    {
      "applier": "94",
      "id": 1095,
      "owner": "L8858",
      "purpose": "WAS-5800: LIMS - DEV",
      "responsible": "S26620",
      "servername": "sv01095"
    },
    {
      "applier": "94",
      "id": 1096,
      "owner": "L8858",
      "purpose": "WAS-5800: LIMS - QA",
      "responsible": "S26620",
      "servername": "sv01096"
    },
    {
      "applier": "AS0500",
      "id": 1097,
      "owner": "H15639",
      "purpose": "SQL Server for Fermas Audit measurements",
      "responsible": "J0649",
      "servername": "sv01097"
    },
    {
      "applier": "AR0279",
      "id": 1098,
      "owner": "D14495",
      "purpose": "EBSILON Professional 13",
      "responsible": "A1912",
      "servername": "sv01098"
    },
    {
      "applier": "AD0233",
      "id": 1099,
      "owner": "H15639",
      "purpose": "IIS, MariaDB",
      "responsible": "H15639",
      "servername": "sv01099"
    },
    {
      "applier": "AR0279",
      "id": 1100,
      "owner": "M1533",
      "purpose": "special switching software for telephony ",
      "responsible": "A1912",
      "servername": "sv01100"
    },
    {
      "applier": "AR0279",
      "id": 1101,
      "owner": "D0106",
      "purpose": "SP4VE-Proxy",
      "responsible": "D18547",
      "servername": "sv01101"
    },
    {
      "applier": "D18547",
      "id": 1102,
      "owner": "D18547",
      "purpose": "vCenter Test envr",
      "responsible": "D18547",
      "servername": "sv01102"
    },
    {
      "applier": "S18344",
      "id": 1103,
      "owner": "W10556",
      "purpose": "MetaSploit Appliance",
      "responsible": "W10556",
      "servername": "sv01103"
    },
    {
      "applier": "S18344",
      "id": 1104,
      "owner": "W10556",
      "purpose": "MetaSploit Appliance",
      "responsible": "W10556",
      "servername": "sv01104"
    },
    {
      "applier": "AS0500",
      "id": 1105,
      "owner": "S25180",
      "purpose": "QA server",
      "responsible": "D18547",
      "servername": "sv01105"
    },
    {
      "applier": "AD0233",
      "id": 1106,
      "owner": "H15639",
      "purpose": "Citrix remote server for ILA portal and RDP",
      "responsible": "H15639",
      "servername": "sv01106"
    },
    {
      "applier": "AD0233",
      "id": 1107,
      "owner": "H15639",
      "purpose": "File Services",
      "responsible": "H15639",
      "servername": "sv01107"
    },
    {
      "applier": "AR0279",
      "id": 1108,
      "owner": "D0106",
      "purpose": "SP-Server ",
      "responsible": "A0423",
      "servername": "sv01108"
    },
    {
      "applier": "AY0017",
      "id": 1109,
      "owner": "T8973",
      "purpose": "ASP-Server SpecialApp Antwerpen",
      "responsible": "A0423",
      "servername": "sv01109"
    },
    {
      "applier": "AY0017",
      "id": 1110,
      "owner": "T8973",
      "purpose": "ASP-Server SpecialApp ",
      "responsible": "A0423",
      "servername": "sv01110"
    },
    {
      "applier": "GA2624",
      "id": 1111,
      "owner": "R1173",
      "purpose": "Spectrum4VE ANT Test #2",
      "responsible": "R1173",
      "servername": "sv01111"
    },
    {
      "applier": "GA2624",
      "id": 1112,
      "owner": "R1173",
      "purpose": "Spectrum4VE ANT Test #1",
      "responsible": "R1173",
      "servername": "sv01112"
    },
    {
      "applier": "AD0233",
      "id": 1113,
      "owner": "H15639",
      "purpose": "WEB Server for eVIS",
      "responsible": "H15639",
      "servername": "sv01113"
    },
    {
      "applier": "AS0500",
      "id": 1114,
      "owner": "T3070",
      "purpose": "RFT00605080",
      "responsible": "D18547",
      "servername": "sv01114"
    },
    {
      "applier": "AY0017",
      "id": 1115,
      "owner": "M22870",
      "purpose": "sFTP file transfer (office2DCS)",
      "responsible": "D15437",
      "servername": "sv01115"
    },
    {
      "applier": "AT0403",
      "id": 1116,
      "owner": "L8858",
      "purpose": "LIMS QA",
      "responsible": "S18344",
      "servername": "sv01116"
    },
    {
      "applier": "AT0403",
      "id": 1117,
      "owner": "L8858",
      "purpose": "LIMS PROD II",
      "responsible": "S18344",
      "servername": "sv01117"
    },
    {
      "applier": "AB0329",
      "id": 1118,
      "owner": "C15512",
      "purpose": "VM Server 2016 for M0515-Site  Worms",
      "responsible": "A0423",
      "servername": "sv01118"
    },
    {
      "applier": "AB0329",
      "id": 1119,
      "owner": "C15512",
      "purpose": "VM Server 2016 M0119-Site Essen",
      "responsible": "A0423",
      "servername": "sv01119"
    },
    {
      "applier": "AB0329",
      "id": 1120,
      "owner": "C15512",
      "purpose": "Installation VM Server 2016 M0114-Site Dossenheim",
      "responsible": "A0423",
      "servername": "sv01120"
    },
    {
      "applier": "A0423",
      "id": 1121,
      "owner": "K0563",
      "purpose": "ClickShare-Pr\u00c3\u00a4sentation Server",
      "responsible": "A0423",
      "servername": "sv01121"
    },
    {
      "applier": "AS0500",
      "id": 1122,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "D18547",
      "servername": "sv01122"
    },
    {
      "applier": "AY0017",
      "id": 1123,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "A0423",
      "servername": "sv01123"
    },
    {
      "applier": "AS0500",
      "id": 1124,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "D18547",
      "servername": "sv01124"
    },
    {
      "applier": "AS0500",
      "id": 1125,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "D18547",
      "servername": "sv01125"
    },
    {
      "applier": "AS0500",
      "id": 1126,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "D18547",
      "servername": "sv01126"
    },
    {
      "applier": "AY0017",
      "id": 1127,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "D15437",
      "servername": "sv01127"
    },
    {
      "applier": "AY0017",
      "id": 1128,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "G12866",
      "servername": "sv01128"
    },
    {
      "applier": "GA2624",
      "id": 1129,
      "owner": "D0106",
      "purpose": "MALSPT - Spectrum Protect Testserver",
      "responsible": "C10477",
      "servername": "sv01129"
    },
    {
      "applier": "GA2624",
      "id": 1130,
      "owner": "D0106",
      "purpose": "MALSPP - Spectrum Protect Proxy",
      "responsible": "C10477",
      "servername": "sv01130"
    },
    {
      "applier": "GA2624",
      "id": 1131,
      "owner": "D0106",
      "purpose": "MALTS1 - Testserver 1",
      "responsible": "C10477",
      "servername": "sv01131"
    },
    {
      "applier": "GA2624",
      "id": 1132,
      "owner": "D0106",
      "purpose": "MALTS2 - Testserver 2",
      "responsible": "C10477",
      "servername": "sv01132"
    },
    {
      "applier": "GA2624",
      "id": 1133,
      "owner": "S19285",
      "purpose": "PoC ThingWorx",
      "responsible": "C1314",
      "servername": "sv01133"
    },
    {
      "applier": "AS0494",
      "id": 1134,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "S26620",
      "servername": "sv01134"
    },
    {
      "applier": "AS0500",
      "id": 1135,
      "owner": "J15936",
      "purpose": "SAP",
      "responsible": "D18547",
      "servername": "sv01135"
    },
    {
      "applier": "AS0500",
      "id": 1136,
      "owner": "J15936",
      "purpose": "SAP",
      "responsible": "D18547",
      "servername": "sv01136"
    },
    {
      "applier": "255",
      "id": 1137,
      "owner": "E8628",
      "purpose": "ApSec Application Server for APAC Region",
      "responsible": "H17255",
      "servername": "sv01137"
    },
    {
      "applier": "AS0494",
      "id": 1138,
      "owner": "M23055",
      "purpose": "Webserver",
      "responsible": "S26620",
      "servername": "sv01138"
    },
    {
      "applier": "AR0279",
      "id": 1139,
      "owner": "E12263",
      "purpose": " AD LDS Server",
      "responsible": "O0067",
      "servername": "sv01139"
    },
    {
      "applier": "AR0279",
      "id": 1140,
      "owner": "E12263",
      "purpose": "AD LDS Server",
      "responsible": "O0067",
      "servername": "sv01140"
    },
    {
      "applier": "AY0017",
      "id": 1141,
      "owner": "M0495",
      "purpose": "domain controller for AD forest MMA.dom",
      "responsible": "O0067",
      "servername": "sv01141"
    },
    {
      "applier": "AY0017",
      "id": 1142,
      "owner": "M0495",
      "purpose": "domain controller for AD forest MMA.dom",
      "responsible": "O0067",
      "servername": "sv01142"
    },
    {
      "applier": "AY0017",
      "id": 1143,
      "owner": "M0495",
      "purpose": "domain controller for AD forest MMA.dom",
      "responsible": "O0067",
      "servername": "sv01143"
    },
    {
      "applier": "\\R19376",
      "id": 1144,
      "owner": "J28219",
      "purpose": "Evoko Liso",
      "responsible": "R19376",
      "servername": "sv01144"
    },
    {
      "applier": "GA2624",
      "id": 1145,
      "owner": "M34002",
      "purpose": "Oracle Database Server",
      "responsible": "C10477",
      "servername": "sv01145"
    },
    {
      "applier": "GA2624",
      "id": 1146,
      "owner": "M34002",
      "purpose": "Oracle Database Server",
      "responsible": "C10477",
      "servername": "sv01146"
    },
    {
      "applier": "GA2624",
      "id": 1147,
      "owner": "M34002",
      "purpose": "Oracle Database Server",
      "responsible": "C10477",
      "servername": "sv01147"
    },
    {
      "applier": "GA2624",
      "id": 1148,
      "owner": "M34002",
      "purpose": "Oracle Database Server",
      "responsible": "C10477",
      "servername": "sv01148"
    },
    {
      "applier": "GA2624",
      "id": 1149,
      "owner": "M34002",
      "purpose": "Oracle Database Server",
      "responsible": "C10477",
      "servername": "sv01149"
    },
    {
      "applier": "GA2624",
      "id": 1150,
      "owner": "M34002",
      "purpose": "Oracle Database Server",
      "responsible": "C10477",
      "servername": "sv01150"
    },
    {
      "applier": "AS0500",
      "id": 1151,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "D18547",
      "servername": "sv01151"
    },
    {
      "applier": "\\M32214",
      "id": 1152,
      "owner": "M32214",
      "purpose": "Test ",
      "responsible": "M32214",
      "servername": "sv01152"
    },
    {
      "applier": "G12866",
      "id": 1153,
      "owner": "G12866",
      "purpose": "ESXi Host",
      "responsible": "G12866",
      "servername": "sv01153"
    },
    {
      "applier": "G12866",
      "id": 1154,
      "owner": "G12866",
      "purpose": "ESXi Host",
      "responsible": "G12866",
      "servername": "sv01154"
    },
    {
      "applier": "AS0494",
      "id": 1155,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "D18547",
      "servername": "sv01155"
    },
    {
      "applier": "AS0494",
      "id": 1156,
      "owner": "C10586",
      "purpose": "Domain Controller",
      "responsible": "D18547",
      "servername": "sv01156"
    },
    {
      "applier": "AT0403",
      "id": 1157,
      "owner": "A1019",
      "purpose": "Blackberry Router",
      "responsible": "S18344",
      "servername": "sv01157"
    },
    {
      "applier": "AT0403",
      "id": 1158,
      "owner": "A1019",
      "purpose": "Blackberry Router",
      "responsible": "D15437",
      "servername": "sv01158"
    },
    {
      "applier": "\\R19376",
      "id": 1159,
      "owner": "D5516",
      "purpose": "2016 Americas Legacy Print Server",
      "responsible": "R19376",
      "servername": "sv01159"
    },
    {
      "applier": "\\R19376",
      "id": 1160,
      "owner": "D5516",
      "purpose": "2016 Americas Legacy Print Server",
      "responsible": "R19376",
      "servername": "sv01160"
    },
    {
      "applier": "G12866",
      "id": 1161,
      "owner": "U0358",
      "purpose": "Spectrum Protect",
      "responsible": "G12866",
      "servername": "sv01161"
    },
    {
      "applier": "AB0329",
      "id": 1162,
      "owner": "L8858",
      "purpose": "Stage: ECM PROD Brava/Blazon",
      "responsible": "A0423",
      "servername": "sv01162"
    },
    {
      "applier": "O0067",
      "id": 1163,
      "owner": "M0495",
      "purpose": "PKI Server Worms",
      "responsible": "O0067",
      "servername": "sv01163"
    },
    {
      "applier": "O0067",
      "id": 1164,
      "owner": "M0495",
      "purpose": "PKI Server Worms",
      "responsible": "O0067",
      "servername": "sv01164"
    },
    {
      "applier": "O0067",
      "id": 1165,
      "owner": "M0495",
      "purpose": "ADFS Server Worms",
      "responsible": "O0067",
      "servername": "sv01165"
    },
    {
      "applier": "O0067",
      "id": 1166,
      "owner": "M0495",
      "purpose": "ADFS Server Worms",
      "responsible": "O0067",
      "servername": "sv01166"
    },
    {
      "applier": "O0067",
      "id": 1167,
      "owner": "M0495",
      "purpose": "ADFS Server Worms",
      "responsible": "O0067",
      "servername": "sv01167"
    },
    {
      "applier": "O0067",
      "id": 1168,
      "owner": "M0495",
      "purpose": "ADFS Server Worms",
      "responsible": "O0067",
      "servername": "sv01168"
    },
    {
      "applier": "O0067",
      "id": 1169,
      "owner": "M0495",
      "purpose": "AADConnect Server Worms",
      "responsible": "O0067",
      "servername": "sv01169"
    },
    {
      "applier": "O0067",
      "id": 1170,
      "owner": "M0495",
      "purpose": "AADConnect Server Worms",
      "responsible": "O0067",
      "servername": "sv01170"
    },
    {
      "applier": "AB0329",
      "id": 1171,
      "owner": "T8973",
      "purpose": "Reinstall MALASP100",
      "responsible": "A0423",
      "servername": "sv01171"
    },
    {
      "applier": "AY0017",
      "id": 1172,
      "owner": "M2129",
      "purpose": "Admin Server Client",
      "responsible": "A0423",
      "servername": "sv01172"
    },
    {
      "applier": "GA2624",
      "id": 1173,
      "owner": "S10454",
      "purpose": "Docker Host",
      "responsible": "B11210",
      "servername": "sv01173"
    },
    {
      "applier": "GA2624",
      "id": 1174,
      "owner": "S19285",
      "purpose": "Oracle Server",
      "responsible": "K15717",
      "servername": "sv01174"
    },
    {
      "applier": "AS0500",
      "id": 1175,
      "owner": "D7746",
      "purpose": "Patchmanagement Server ",
      "responsible": "O0067",
      "servername": "sv01175"
    },
    {
      "applier": "\\R19376",
      "id": 1176,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "R19376",
      "servername": "sv01176"
    },
    {
      "applier": "382",
      "id": 1177,
      "owner": "M39382",
      "purpose": "TSM Server Singapore Hubsite",
      "responsible": "M39382",
      "servername": "sv01177"
    },
    {
      "applier": "AB0329",
      "id": 1178,
      "owner": "H2347",
      "purpose": "Arigon Application Server",
      "responsible": "O0067",
      "servername": "sv01178"
    },
    {
      "applier": "S18344",
      "id": 1179,
      "owner": "B0163",
      "purpose": "Opentext Archiv Server",
      "responsible": "S18344",
      "servername": "sv01179"
    },
    {
      "applier": "AB0329",
      "id": 1180,
      "owner": "C15512",
      "purpose": "domain controller for MADRID gatekeeper carveout",
      "responsible": "O0067",
      "servername": "sv01180"
    },
    {
      "applier": "AR0279",
      "id": 1181,
      "owner": "M6364",
      "purpose": "Connector for Opengear and Avocent Remote",
      "responsible": "O0067",
      "servername": "sv01181"
    },
    {
      "applier": "AR0279",
      "id": 1182,
      "owner": "D0106",
      "purpose": "Spectrum Protect for Virtual Environment ",
      "responsible": "O0067",
      "servername": "sv01182"
    },
    {
      "applier": "AS0500",
      "id": 1183,
      "owner": "F1768",
      "purpose": "RFT00633302",
      "responsible": "D18547",
      "servername": "sv01183"
    },
    {
      "applier": "AS0500",
      "id": 1184,
      "owner": "F1768",
      "purpose": "RFT00633302",
      "responsible": "D18547",
      "servername": "sv01184"
    },
    {
      "applier": "\\R19376",
      "id": 1185,
      "owner": "W2146",
      "purpose": "GSO Terminal Server",
      "responsible": "R19376",
      "servername": "sv01185"
    },
    {
      "applier": "\\R19376",
      "id": 1186,
      "owner": "W2146",
      "purpose": "GSO Terminal Server",
      "responsible": "R19376",
      "servername": "sv01186"
    },
    {
      "applier": "AB0329",
      "id": 1187,
      "owner": "D1414",
      "purpose": "APC Online 1",
      "responsible": "O0067",
      "servername": "sv01187"
    },
    {
      "applier": "AB0329",
      "id": 1188,
      "owner": "D1414",
      "purpose": "APC Online 2",
      "responsible": "O0067",
      "servername": "sv01188"
    },
    {
      "applier": "AB0329",
      "id": 1189,
      "owner": "D1414",
      "purpose": "APC Online 3",
      "responsible": "O0067",
      "servername": "sv01189"
    },
    {
      "applier": "AB0329",
      "id": 1190,
      "owner": "D1414",
      "purpose": "APC RTO",
      "responsible": "O0067",
      "servername": "sv01190"
    },
    {
      "applier": "AB0329",
      "id": 1191,
      "owner": "D1414",
      "purpose": "APC Watch",
      "responsible": "O0067",
      "servername": "sv01191"
    },
    {
      "applier": "AB0329",
      "id": 1192,
      "owner": "D1414",
      "purpose": "APC Web",
      "responsible": "O0067",
      "servername": "sv01192"
    },
    {
      "applier": "AS0500",
      "id": 1193,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "D18547",
      "servername": "sv01193"
    },
    {
      "applier": "AD0233",
      "id": 1194,
      "owner": "C15512",
      "purpose": "Domain Controller",
      "responsible": "C15512",
      "servername": "sv01194"
    },
    {
      "applier": "AD0233",
      "id": 1195,
      "owner": "D0106",
      "purpose": "Proxy Server",
      "responsible": "D0106",
      "servername": "sv01195"
    }
  ]
}
'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
