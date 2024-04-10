#!/user/bin/python
# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2020 replay file
# Internal Version: 2019_09_14-01.49.31 163176
# Run by bmyy on Mon May 22 10:16:35 2023
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *

session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=198.749984741211,
                 height=121.592582702637)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
from abaqus import *
from abaqusConstants import *
from odbAccess import *
from visualization import *
import string
import xlwt
import time



executeOnCaeStartup()
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)

# ----------------------------------保存模型位置---------------------------------------------------------------------------
import os
H_thickness = [4.74, 9.95, 5.18, 6.55, 6.91, 5.04, 4.42, 5.31, 7.41, 9.07, 9.11, 7.08, 9.6, 4.88, 7.29, 8.4, 8.58, 7.76,
               5.64, 9.42, 6.28, 4.66, 6.39, 7.19, 4.04, 5.43, 8.82, 8.54, 4.3, 6.09, 5.24, 4.82, 8.05, 6.46, 9.69,
               7.85, 9.9, 4.57, 7.5, 5.82, 8.63, 4.5, 7.6, 6.81, 6.01, 5.72, 6.72, 5.78, 8.68, 4.06, 8.79, 5.58, 8.98,
               7.72, 9.79, 6.64, 6.13, 9.25, 6.64, 6.99, 6.17, 9.51, 4.44, 8.15, 4.31, 5.91, 4.64, 4.22, 9.3, 9.39,
               7.13, 9.76, 4.97, 5.36, 9.88, 9.55, 8.12, 8.0, 7.83, 4.9, 5.54, 6.86, 8.37, 8.31, 5.97, 7.95, 8.88, 8.25,
               7.44, 7.61, 8.99, 7.32, 6.22, 5.1, 4.18, 7.03, 8.48, 9.22, 5.48, 6.49]
#H_thickness = H_thickness[148:]
Distance = [1.65, 0.72, 1.23, 1.05, 0.52, 1.51, 1.32, 0.83, 1.2, 1.33, 0.93, 1.8, 0.44, 0.99, 0.42, 1.31, 1.5, 1.87,
            1.97, 1.06, 1.26, 0.79, 1.08, 0.62, 1.11, 1.04, 1.15, 1.48, 1.13, 0.6, 0.91, 1.66, 1.83, 0.38, 0.76, 1.27,
            1.7, 0.58, 1.72, 1.56, 0.48, 1.01, 0.64, 1.94, 1.46, 0.36, 0.82, 0.97, 1.18, 1.95, 0.88, 0.8, 0.65, 0.57,
            1.4, 0.53, 1.9, 1.35, 0.87, 0.69, 1.42, 1.28, 1.43, 0.7, 0.77, 1.37, 1.17, 0.41, 0.73, 1.91, 0.48, 1.63,
            1.45, 0.95, 1.76, 2.0, 1.22, 1.78, 1.54, 0.68, 0.91, 1.85, 1.81, 0.56, 1.61, 1.59, 0.46, 1.6, 1.74, 1.68,
            1.93, 1.72, 0.86, 1.01, 1.86, 1.1, 0.39, 1.38, 1.53, 0.51]
#Distance = Distance[148:]
K_width = [6.85, 2.76, 7.8, 2.08, 2.7, 9.82, 4.57, 9.9, 5.84, 4.79, 9.53, 6.44, 2.37, 3.85, 8.45, 9.93, 5.09, 3.31,
           3.61, 9.73, 4.66, 3.94, 8.09, 7.3, 9.08, 8.02, 8.34, 4.3, 5.17, 5.29, 9.21, 6.01, 2.84, 6.34, 9.6, 4.04,
           4.19, 6.73, 7.74, 2.24, 3.48, 8.74, 9.29, 8.26, 8.21, 5.69, 3.38, 5.45, 3.79, 6.28, 6.19, 8.7, 4.54, 8.98,
           7.05, 2.51, 6.9, 5.36, 7.03, 5.24, 3.02, 4.36, 8.93, 2.12, 3.75, 3.14, 9.14, 7.65, 2.17, 7.53, 5.93, 7.92,
           7.37, 4.92, 7.27, 3.24, 3.1, 7.16, 6.14, 9.47, 5.01, 7.95, 5.88, 4.87, 2.91, 8.49, 3.57, 8.85, 6.49, 2.61,
           8.61, 7.5, 5.61, 5.55, 6.68, 4.15, 9.37, 2.45, 4.44, 6.61]
#K_width=K_width[148:]
Y_thickness = [16.2, 4.86, 18.08, 10.1, 17.13, 9.13, 19.18, 9.95, 10.59, 13.2, 12.54, 14.76, 6.9, 16.06, 16.54, 15.82,
               15.23, 7.27, 9.02, 5.43, 8.41, 12.15, 13.7, 8.83, 8.74, 8.17, 10.25, 14.57, 4.3, 17.34, 5.53, 14.48,
               17.62, 7.12, 18.89, 11.71, 16.84, 13.9, 11.27, 9.85, 6.61, 7.4, 6.07, 11.43, 15.0, 5.06, 6.1, 6.52,
               19.38, 15.57, 18.06, 15.85, 19.77, 16.65, 13.51, 5.81, 7.75, 18.37, 13.33, 12.96, 15.41, 4.65, 8.13,
               19.88, 16.46, 15.04, 10.52, 9.56, 18.66, 7.91, 19.61, 17.57, 14.16, 11.13, 11.57, 5.66, 4.6, 13.95, 6.72,
               10.8, 8.58, 10.9, 4.04, 11.97, 12.31, 12.71, 18.86, 4.39, 7.59, 9.29, 18.53, 13.08, 14.35, 5.19, 17.85,
               6.32, 19.35, 12.35, 17.02, 9.75]
#Y_thickness=Y_thickness[148:]
EE = [236247.43, 212137.8, 42644.69, 142148.71, 177665.68, 242524.23, 235117.56, 179765.82, 149865.08, 229605.6,
      240413.9, 221452.69, 185874.85, 172418.23, 163497.17, 106413.56, 153705.53, 157967.33, 246891.19, 104971.02,
      145342.95, 132287.06, 202572.51, 167031.57, 134811.85, 164895.7, 54089.34, 110996.19, 79239.2, 96749.48,
      108615.41, 205729.88, 64380.74, 58594.4, 96375.95, 218725.2, 216694.95, 123642.6, 187031.9, 45337.68, 83189.02,
      207698.03, 172017.2, 124778.57, 191957.54, 117284.05, 86950.89, 93060.19, 74745.29, 61960.37, 143026.15,
      100156.53, 200225.38, 189286.54, 88465.1, 139044.2, 213965.38, 199599.1, 228659.12, 121672.19, 68131.53, 81180.74,
      225697.12, 101977.92, 67284.55, 70047.38, 222936.29, 238532.22, 193630.62, 56012.13, 151927.1, 126661.47,
      49438.01, 157213.16, 129879.72, 112155.11, 161797.42, 85270.8, 175717.3, 183197.17, 133911.87, 244220.44,
      215812.08, 196992.18, 72573.92, 138681.02, 114414.63, 91220.01, 46942.4, 118709.99, 148034.31, 231930.8, 41880.8,
      76924.07, 169871.42, 52500.73, 208503.2, 59864.56, 248650.64, 181512.3]
#EE=EE[148:]
UUU = [0.26, 0.2, 0.3, 0.34, 0.25, 0.37, 0.33, 0.22, 0.33, 0.21, 0.23, 0.36, 0.29, 0.22, 0.22, 0.23, 0.22, 0.31, 0.32,
       0.31, 0.35, 0.31, 0.22, 0.28, 0.32, 0.39, 0.22, 0.21, 0.37, 0.33, 0.36, 0.27, 0.28, 0.26, 0.32, 0.27, 0.3, 0.21,
       0.28, 0.39, 0.38, 0.31, 0.31, 0.37, 0.25, 0.24, 0.38, 0.36, 0.24, 0.26, 0.37, 0.24, 0.25, 0.39, 0.34, 0.38, 0.33,
       0.27, 0.36, 0.29, 0.32, 0.2, 0.38, 0.4, 0.34, 0.27, 0.39, 0.38, 0.23, 0.26, 0.35, 0.29, 0.29, 0.21, 0.35, 0.2,
       0.33, 0.35, 0.4, 0.23, 0.24, 0.29, 0.34, 0.36, 0.3, 0.31, 0.34, 0.37, 0.28, 0.25, 0.28, 0.27, 0.26, 0.27, 0.38,
       0.32, 0.24, 0.4, 0.3, 0.23]
#UUU=UUU[148:]
RR = [466.99, 362.9, 41.17, 59.59, 211.86, 366.92, 384.87, 154.97, 176.03, 303.42, 294.98, 498.54, 47.84, 442.33,
      128.04, 357.06, 257.01, 332.84, 269.62, 341.43, 403.67, 283.77, 230.52, 169.77, 317.95, 376.64, 125.1, 409.69,
      334.7, 247.88, 237.78, 121.9, 479.39, 487.37, 240.45, 106.85, 307.6, 199.18, 314.24, 456.71, 220.61, 345.33,
      375.2, 321.68, 147.14, 65.42, 94.41, 187.05, 291.6, 82.25, 54.56, 418.65, 261.42, 348.85, 329.11, 224.7, 416.74,
      494.63, 139.09, 181.96, 167.75, 395.34, 143.98, 254.09, 459.92, 447.09, 471.31, 70.93, 271.9, 112.51, 208.64,
      205.06, 387.51, 86.74, 104.03, 284.22, 358.4, 214.83, 391.75, 242.56, 50.74, 188.78, 195.71, 99.19, 482.48,
      115.91, 423.55, 134.16, 297.95, 433.36, 80.81, 73.08, 428.25, 277.33, 158.94, 449.62, 474.77, 398.91, 437.12,
      162.0]
#RR=RR[148:]
QQ = [192.49, 13.64, 58.56, 186.63, 171.97, 27.21, 38.32, 115.55, 86.69, 190.76, 19.87, 45.29, 143.56, 34.19, 126.78,
      72.74, 169.97, 151.22, 84.25, 160.03, 30.5, 132.68, 105.44, 153.5, 54.28, 55.66, 66.35, 178.99, 50.71, 97.05,
      38.95, 108.08, 181.81, 165.6, 146.95, 109.87, 15.74, 43.37, 120.51, 77.19, 68.21, 75.57, 137.23, 163.32, 52.98,
      88.21, 101.66, 79.08, 111.57, 129.49, 196.51, 134.85, 18.35, 59.55, 198.52, 83.72, 188.58, 42.06, 155.21, 47.98,
      14.77, 130.74, 158.08, 10.34, 62.76, 139.49, 92.48, 49.53, 138.48, 22.99, 72.35, 183.61, 161.11, 143.0, 118.88,
      174.64, 69.03, 98.72, 165.92, 90.37, 81.35, 149.58, 176.33, 104.85, 32.3, 64.68, 25.46, 117.63, 100.27, 195.15,
      180.45, 94.63, 122.32, 189.65, 112.68, 168.82, 124.14, 145.27, 24.49, 36.03]
#QQ=QQ[148:]
BB = [7.55, 2.7, 8.25, 9.3, 2.74, 9.74, 3.62, 7.6, 5.06, 3.49, 7.2, 1.96, 4.4, 1.64, 4.57, 4.05, 5.82, 1.83, 1.16, 2.08,
      6.58, 8.9, 5.88, 3.26, 4.87, 1.41, 6.02, 8.97, 3.37, 2.82, 3.7, 8.14, 2.51, 9.41, 6.86, 7.06, 2.93, 3.53, 1.59,
      6.66, 5.01, 3.2, 1.3, 5.27, 9.95, 9.07, 3.96, 3.07, 9.15, 1.47, 6.18, 9.85, 8.71, 9.52, 7.32, 4.13, 1.18, 6.43,
      7.81, 5.76, 4.73, 9.62, 2.35, 6.23, 8.62, 2.21, 6.73, 7.91, 5.52, 6.09, 6.97, 4.3, 9.21, 2.27, 4.87, 5.45, 5.38,
      1.74, 2.05, 4.19, 6.76, 3.83, 6.38, 7.95, 4.45, 4.63, 7.24, 8.81, 8.48, 7.74, 8.35, 9.7, 8.45, 5.17, 1.06, 3.05,
      8.08, 7.4, 2.58, 5.6]
#BB=BB[148:]
C1 = [12722.59, 9756.46, 3316.46, 21854.73, 25709.94, 9034.93, 11774.59, 5950.37, 4311.68, 23550.67, 1530.91, 26385.71,
      2005.82, 8501.57, 5727.58, 24106.3, 20446.19, 10862.43, 7195.54, 27634.99, 1791.94, 28140.1, 3815.89, 28604.82,
      18963.69, 4105.15, 9171.35, 25402.15, 3002.92, 29926.19, 6591.36, 17296.48, 22486.67, 29570.78, 21371.69,
      11153.17, 7802.57, 8662.1, 24369.48, 26863.95, 14810.31, 17779.47, 4815.56, 16495.56, 28379.21, 24921.62,
      25189.09, 15332.59, 9550.68, 20136.5, 12432.56, 29141.18, 18537.89, 25973.57, 2652.76, 16821.12, 10486.17,
      29007.94, 8008.18, 20362.3, 19844.79, 18152.69, 3498.49, 21966.23, 13750.92, 14290.64, 10588.57, 22380.91,
      24592.15, 19124.26, 20846.99, 13785.45, 27345.21, 4605.37, 18091.55, 22898.86, 7393.72, 12138.05, 16199.08,
      5601.83, 21149.91, 6806.57, 15907.23, 13017.98, 13206.35, 6253.16, 17041.89, 1281.34, 23750.6, 23289.46, 15188.36,
      19497.8, 2431.1, 27777.98, 11718.66, 15710.84, 5128.79, 26636.56, 10042.95, 14400.63]
#C1=C1[148:]
C2 = [9519.4, 620.96, 10861.82, 4317.36, 1311.19, 9099.81, 9707.29, 10637.38, 1869.2, 11767.26, 3473.74, 10073.43,
      8521.77, 11269.86, 10388.36, 6027.58, 11315.78, 8565.3, 3516.7, 9876.37, 8313.97, 9455.08, 1455.62, 9176.26,
      11920.64, 1169.94, 2290.36, 7086.15, 7644.54, 4051.97, 9350.44, 10766.57, 1022.87, 7991.41, 8419.39, 3738.76,
      895.42, 6773.47, 6319.02, 8685.82, 4291.09, 7329.23, 3675.58, 5719.78, 1279.4, 5503.05, 830.91, 4076.5, 10223.45,
      7603.2, 4711.52, 6951.54, 2460.44, 4855.51, 4446.29, 5437.34, 3193.82, 10565.03, 4625.77, 5562.56, 4945.84,
      516.39, 9653.04, 8809.04, 2615.93, 2359.73, 8189.49, 2870.89, 5241.34, 10970.87, 11584.05, 10411.36, 7425.14,
      3905.07, 1903.44, 7827.11, 11123.73, 3073.9, 5119.9, 1760.33, 2786.13, 9962.73, 2918.5, 6428.85, 5043.54, 11445.1,
      7225.93, 6203.72, 3306.54, 1619.33, 5855.5, 7866.67, 11822.08, 6550.68, 8998.97, 2199.73, 6651.29, 2031.89,
      6859.41, 5905.72]
#C2=C2[148:]
C3 = [4418.99, 4140.61, 7507.66, 1828.02, 6581.65, 6426.54, 9923.69, 3550.04, 9169.38, 3139.95, 9808.94, 227.81, 8027.0,
      3648.86, 1481.4, 8797.38, 1275.19, 696.48, 1150.04, 1884.51, 3713.63, 9709.0, 9092.5, 2183.44, 3035.16, 9607.87,
      5707.3, 5289.48, 2498.36, 493.94, 9558.25, 6942.78, 5866.84, 2591.24, 2764.59, 2087.93, 4708.07, 7732.3, 9282.9,
      5445.9, 6439.48, 5585.15, 4866.38, 8320.41, 161.47, 8442.6, 3422.47, 5196.0, 6807.89, 4345.25, 4492.83, 650.75,
      3811.1, 8267.57, 6237.26, 6710.63, 7852.13, 7385.08, 7141.81, 4199.45, 8145.15, 5115.9, 5950.34, 2942.21, 815.23,
      9415.86, 4629.0, 2865.32, 565.12, 8978.77, 5457.08, 966.7, 4754.14, 2467.63, 348.07, 2322.81, 1297.21, 8014.84,
      8702.94, 6875.95, 6310.52, 5008.44, 3256.38, 5788.93, 7603.31, 7071.14, 7313.0, 4021.67, 1590.12, 3892.29, 1569.6,
      9403.02, 8890.82, 994.3, 3356.24, 1742.48, 2056.42, 7626.02, 6111.32, 8571.18]
#C3=C3[148:]
Gama1 = [354.54, 1212.17, 20.23, 949.51, 176.84, 129.49, 1443.73, 43.92, 575.97, 314.12, 852.39, 366.57, 200.91,
         1499.44, 426.57, 61.04, 695.88, 1015.15, 393.63, 855.37, 1040.26, 1158.05, 1351.72, 254.94, 1142.31, 895.36,
         380.4, 162.96, 670.19, 801.68, 1098.66, 598.33, 1179.63, 902.32, 80.49, 1481.25, 319.54, 679.82, 1267.93,
         290.31, 658.45, 1412.79, 335.09, 740.88, 760.48, 992.57, 521.35, 465.21, 1113.68, 872.56, 1258.52, 1393.87,
         147.96, 1426.16, 1306.12, 9.1, 718.11, 497.73, 1335.48, 488.52, 729.55, 1455.59, 541.88, 1278.95, 1092.24,
         1403.92, 980.04, 256.49, 935.01, 1331.22, 104.16, 961.05, 1067.63, 1244.04, 441.24, 836.96, 618.64, 235.0,
         1134.14, 46.71, 450.78, 526.44, 189.34, 567.52, 603.48, 640.42, 416.11, 1058.64, 774.83, 281.26, 1223.38,
         1026.92, 810.96, 106.77, 1195.56, 927.11, 1292.83, 216.54, 1374.98, 792.84]
#Gama1=Gama1[148:]
Gama2 = [259.72, 610.01, 373.07, 816.81, 246.22, 758.92, 896.27, 170.69, 889.06, 623.34, 918.3, 556.55, 85.18, 62.13,
         486.8, 468.91, 283.04, 947.1, 534.19, 513.97, 208.47, 736.25, 823.28, 332.08, 877.13, 721.69, 933.32, 344.48,
         574.91, 731.4, 678.24, 197.27, 401.78, 594.77, 862.8, 419.74, 650.39, 367.59, 155.71, 584.94, 300.01, 848.22,
         53.04, 464.56, 354.31, 781.2, 833.44, 488.64, 178.86, 235.63, 809.99, 92.05, 102.72, 386.46, 907.76, 700.79,
         782.92, 571.19, 846.73, 117.88, 694.22, 637.0, 647.98, 323.28, 312.6, 401.24, 219.67, 612.2, 766.25, 148.86,
         875.18, 129.5, 444.7, 673.26, 141.68, 114.18, 935.62, 296.01, 428.29, 953.36, 501.27, 346.53, 274.71, 435.69,
         520.18, 545.64, 77.0, 189.06, 993.4, 251.63, 793.73, 660.21, 221.44, 986.26, 708.79, 456.88, 978.75, 535.52,
         751.32, 970.38]
#Gama2=Gama2[148:]
Gama3 = [1135.26, 798.99, 104.75, 755.05, 1206.26, 467.44, 1238.42, 507.69, 560.82, 191.98, 957.26, 410.52, 1229.34,
         1314.98, 1413.67, 428.5, 228.8, 1039.96, 1375.77, 1119.37, 333.57, 394.49, 355.02, 841.99, 235.69, 639.94,
         1246.9, 23.24, 211.69, 306.74, 871.02, 121.47, 1274.9, 263.83, 1181.81, 1144.82, 522.75, 488.53, 1364.03,
         542.66, 857.56, 985.04, 57.07, 618.79, 1158.52, 1112.19, 810.75, 900.63, 729.32, 474.53, 310.34, 52.2, 923.44,
         1453.81, 77.54, 964.29, 1086.01, 148.87, 700.65, 1350.44, 936.11, 423.45, 1030.04, 597.84, 248.5, 656.53,
         371.83, 37.14, 1281.82, 1387.57, 670.92, 162.05, 784.2, 130.58, 572.01, 687.02, 1461.21, 86.09, 1081.63,
         625.67, 917.5, 1406.97, 746.91, 1498.73, 715.38, 278.3, 1326.74, 828.96, 1001.94, 1058.08, 1017.49, 585.79,
         1484.16, 339.94, 1296.89, 875.85, 1187.47, 456.35, 1427.9, 185.84
         ]
#Gama3=Gama3[148:]
MC = [0.22, 0.18, 0.25, 0.01, 0.15, 0.2, 0.0, 0.04, 0.2, 0.12, 0.21, 0.05, 0.11, 0.24, 0.0, 0.01, 0.23, 0.06, 0.17,
      0.03, 0.18, 0.15, 0.08, 0.07, 0.19, 0.04, 0.12, 0.24, 0.05, 0.15, 0.16, 0.14, 0.14, 0.17, 0.04, 0.22, 0.02, 0.1,
      0.14, 0.09, 0.07, 0.13, 0.02, 0.09, 0.03, 0.01, 0.15, 0.18, 0.19, 0.06, 0.13, 0.21, 0.16, 0.19, 0.17, 0.16, 0.1,
      0.09, 0.2, 0.21, 0.25, 0.06, 0.03, 0.23, 0.05, 0.02, 0.07, 0.04, 0.08, 0.09, 0.02, 0.1, 0.16, 0.05, 0.1, 0.22,
      0.24, 0.17, 0.11, 0.13, 0.2, 0.03, 0.23, 0.13, 0.07, 0.23, 0.22, 0.01, 0.21, 0.18, 0.12, 0.14, 0.19, 0.24, 0.08,
      0.06, 0.12, 0.11, 0.08, 0.11]
#MC=MC[148:]
K_l = [35, 50, 80]
K_num = [4, 3, 2]
jobn = 0
for k_l, k_num in zip(K_l, K_num):
    for h_t, dis,  y_t, ee, uuu, rr, qq, bb, c1, c2, c3, gama1, gama2, gama3, mc,k_w in \
            zip(H_thickness, Distance, Y_thickness, EE, UUU, RR, QQ, BB, C1, C2, C3, Gama1, Gama2, Gama3, MC,K_width):


        Mdb()
        jobn = jobn + 1
        jobname = "job-{}".format(jobn)

        os.makedirs(r"D:\abaqusmoxingshuju\pythonshuanghexin0\hexinhou-distance-yuesuhou-Hcailiao-Ycailiao-K_num{}"
                    .format(str(h_t) + '-' + str(dis) + '-' + str(y_t)+'-'+str(ee)+'-'+str(uuu)+'-'+str(k_num)))
        os.chdir(r"D:\abaqusmoxingshuju\pythonshuanghexin0\hexinhou-distance-yuesuhou-Hcailiao-Ycailiao-K_num{}"
                 .format(str(h_t) + '-' + str(dis) + '-' + str(y_t)+'-'+str(ee)+'-'+str(uuu)+'-'+str(k_num)))
        mdb.saveAs(pathName='D:/abaqusmoxingshuju/pythonshuanghexin0/hexinhou-distance-yuesuhou-Hcailiao-Ycailiao-K_num{}/moxing{}'
                   .format(str(h_t) + '-' + str(dis) + '-' + str(y_t)+'-'+str(ee)+'-'+str(uuu)+'-'+str(k_num),
                           str(h_t) + '-' + str(dis) + '-' + str(y_t)+'-'+str(ee)+'-'+str(uuu)+'-'+str(k_num)))

        #: 模型数据库已保存到 "F:\abaqusmoxingshuju\pythonshuanghexin\moxing1.cae".

        # ----------------------------------创建模型构件-------------------------------------------------------------------
        s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
                                                     sheetSize=500.0)
        g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
        s1.setPrimaryObject(option=STANDALONE)
        s1.Line(point1=(0.0, 12.5), point2=(-195.0, 12.5))
        s1.HorizontalConstraint(entity=g[2], addUndoState=False)
        session.viewports['Viewport: 1'].view.setValues(nearPlane=404.629,
                                                        farPlane=538.18, width=732.799, height=327.571,
                                                        cameraPosition=(26.9736,
                                                                        5.48879, 471.405),
                                                        cameraTarget=(26.9736, 5.48879, 0))
        s1.Line(point1=(-195.0, 12.5), point2=(-205.0, 22.5))
        s1.Line(point1=(-205.0, 22.5), point2=(-250.0, 22.5))
        s1.HorizontalConstraint(entity=g[4], addUndoState=False)
        s1.Line(point1=(-250.0, 22.5), point2=(-250.0, 0.0))
        s1.VerticalConstraint(entity=g[5], addUndoState=False)
        s1.PerpendicularConstraint(entity1=g[4], entity2=g[5], addUndoState=False)
        s1.Line(point1=(0.0, 0.0), point2=(0.0, -17.5))
        s1.VerticalConstraint(entity=g[6], addUndoState=False)
        s1.Line(point1=(0.0, 0.0), point2=(17.5, 0.0))
        s1.HorizontalConstraint(entity=g[7], addUndoState=False)
        s1.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
        s1.copyMirror(mirrorLine=g[6], objectList=(g[2], g[3], g[4], g[5]))
        s1.copyMirror(mirrorLine=g[7], objectList=(g[2], g[3], g[4], g[5], g[8], g[9],
                                                   g[10], g[11]))
        session.viewports['Viewport: 1'].view.setValues(nearPlane=443.324,
                                                        farPlane=499.485, width=272.289, height=121.717,
                                                        cameraPosition=(21.0533,
                                                                        1.41823, 471.405),
                                                        cameraTarget=(21.0533, 1.41823, 0))
        s1.delete(objectList=(g[7], g[6]))
        s1.FilletByRadius(radius=5.0, curve1=g[2], nearPoint1=(-172.85319519043,
                                                               11.7284698486328), curve2=g[3],
                          nearPoint2=(-199.06477355957,
                                      19.4637756347656))

        s1.FilletByRadius(radius=5.0, curve1=g[8], nearPoint1=(179.811569213867,
                                                               12.9185180664063), curve2=g[9],
                          nearPoint2=(201.853134155273,
                                      17.0836791992188))
        s1.FilletByRadius(radius=5.0, curve1=g[12], nearPoint1=(-171.066055297852,
                                                                -12.0724792480469), curve2=g[13],
                          nearPoint2=(-202.639083862305,
                                      -18.6177368164063))
        s1.FilletByRadius(radius=5.0, curve1=g[16], nearPoint1=(166.110061645508,
                                                                -10.2873992919922), curve2=g[17],
                          nearPoint2=(201.215942382813,
                                      -19.0696449279785))
        p = mdb.models['Model-1'].Part(name='hexin', dimensionality=THREE_D,
                                       type=DEFORMABLE_BODY)
        p = mdb.models['Model-1'].parts['hexin']
        ###########################################################################################################
        p.BaseSolidExtrude(sketch=s1, depth=h_t)

        s1.unsetPrimaryObject()
        p = mdb.models['Model-1'].parts['hexin']
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        del mdb.models['Model-1'].sketches['__profile__']

        # 创建切削
        p = mdb.models['Model-1'].parts['hexin']
        f, e = p.faces, p.edges
        t = p.MakeSketchTransform(sketchPlane=f[16], sketchUpEdge=e[14],
                                  sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0, 4.74))
        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
                                                    sheetSize=1004.08, gridSpacing=25.1, transform=t)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=SUPERIMPOSE)
        p = mdb.models['Model-1'].parts['hexin']
        p.projectReferencesOntoSketch(sketch=s, filter=COPLANAR_EDGES)
        # 开孔画线-1###########################################################################
        s.Line(point1=(-177.5, k_w / 2), point2=(-177.5 + k_l - 5, k_w / 2))
        s.HorizontalConstraint(entity=g[22], addUndoState=False)
        #########################################################################################
        s.Line(point1=(-177.5, -k_w / 2), point2=(-177.5 + k_l - 5, -k_w / 2))
        s.HorizontalConstraint(entity=g[23], addUndoState=False)

        # 画圆弧-1###############################################################################
        s.ArcByStartEndTangent(point1=(-177.5, k_w / 2), point2=(-177.5, -k_w / 2),
                               entity=g[22])
        #####################################################################
        s.ArcByStartEndTangent(point1=(-177.5 + k_l - 5, k_w / 2), point2=(-177.5 + k_l - 5, -k_w / 2),
                               entity=g[22])

        # 开孔画线-2#################################################################################
        s.Line(point1=(177.5, k_w / 2), point2=(177.5 - k_l + 5, k_w / 2))
        s.HorizontalConstraint(entity=g[26], addUndoState=False)
        ###############################################################################################
        s.Line(point1=(177.5, -k_w / 2), point2=(177.5 - k_l + 5, -k_w / 2))
        s.HorizontalConstraint(entity=g[27], addUndoState=False)

        # 画圆弧-2######################################################################
        s.ArcByStartEndTangent(point1=(177.5 - k_l + 5, k_w / 2), point2=(177.5 - k_l + 5, -k_w / 2),
                               entity=g[26])
        ######################################################################################
        s.ArcByStartEndTangent(point1=(177.5, k_w / 2), point2=(177.5, -k_w / 2),
                               entity=g[26])

        # 阵列左端开孔########################################################################
        s.linearPattern(geomList=(g[22], g[23], g[24], g[25]), vertexList=(),
                        number1=k_num, spacing1=k_l + 10, angle1=0.0, number2=1, spacing2=100.409,
                        angle2=90.0)

        # 阵列右端开孔###############################################################
        s.linearPattern(geomList=(g[26], g[27], g[28], g[29]), vertexList=(),
                        number1=k_num, spacing1=k_l + 10, angle1=180.0, number2=1, spacing2=100.409,
                        angle2=90.0)

        # 按草图开孔
        p = mdb.models['Model-1'].parts['hexin']
        f1, e1 = p.faces, p.edges
        p.CutExtrude(sketchPlane=f1[16], sketchUpEdge=e1[10], sketchPlaneSide=SIDE1,
                     sketchOrientation=RIGHT, sketch=s, flipExtrudeDirection=OFF)
        s.unsetPrimaryObject()
        del mdb.models['Model-1'].sketches['__profile__']

        # 构件连接板
        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=45.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)
        s.rectangle(point1=(0.0, 0.0), point2=(45.0, 45.0))
        p = mdb.models['Model-1'].Part(name='lianjieban', dimensionality=THREE_D,
                                       type=DEFORMABLE_BODY)
        p = mdb.models['Model-1'].parts['lianjieban']

        p.BaseSolidExtrude(sketch=s, depth=y_t+2*dis)

        s.unsetPrimaryObject()

        # 构件垫板
        p = mdb.models['Model-1'].parts['lianjieban']
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        del mdb.models['Model-1'].sketches['__profile__']
        s1 = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
                                                     sheetSize=400.0)
        g, v, d, c = s1.geometry, s1.vertices, s1.dimensions, s1.constraints
        s1.setPrimaryObject(option=STANDALONE)

        s1.Line(point1=(0.0, 33.5), point2=(-200.0, 33.5))
        s1.HorizontalConstraint(entity=g[2], addUndoState=False)

        s1.Line(point1=(-200.0, 33.5), point2=(-200.0, 25.0))
        s1.VerticalConstraint(entity=g[3], addUndoState=False)
        s1.PerpendicularConstraint(entity1=g[2], entity2=g[3], addUndoState=False)
        s1.Line(point1=(-200.0, 25.0), point2=(-188.5, 13.5))
        s1.Line(point1=(-188.5, 13.5), point2=(0.0, 13.5))
        s1.HorizontalConstraint(entity=g[5], addUndoState=False)
        s1.Line(point1=(0.0, 0.0), point2=(0.0, -15.0))
        s1.VerticalConstraint(entity=g[6], addUndoState=False)
        s1.Line(point1=(0.0, 0.0), point2=(22.5, 0.0))
        s1.HorizontalConstraint(entity=g[7], addUndoState=False)
        s1.PerpendicularConstraint(entity1=g[6], entity2=g[7], addUndoState=False)
        s1.copyMirror(mirrorLine=g[6], objectList=(g[2], g[3], g[4], g[5]))

        s1.copyMirror(mirrorLine=g[7], objectList=(g[2], g[3], g[4], g[5], g[8], g[9],
                                                   g[10], g[11]))

        s1.delete(objectList=(g[7], g[6]))
        p = mdb.models['Model-1'].Part(name='dianbann', dimensionality=THREE_D,
                                       type=DEFORMABLE_BODY)
        p = mdb.models['Model-1'].parts['dianbann']

        p.BaseSolidExtrude(sketch=s1, depth=h_t+2*dis)

        s1.unsetPrimaryObject()
        # 构件约束板

        p = mdb.models['Model-1'].parts['dianbann']
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        del mdb.models['Model-1'].sketches['__profile__']
        s = mdb.models['Model-1'].ConstrainedSketch(name='__profile__',
                                                    sheetSize=400.0)
        g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
        s.setPrimaryObject(option=STANDALONE)

        s.rectangle(point1=(400.0, 67.0), point2=(0.0, 0.0))
        p = mdb.models['Model-1'].Part(name='yueshuban', dimensionality=THREE_D,
                                       type=DEFORMABLE_BODY)
        p = mdb.models['Model-1'].parts['yueshuban']

        p.BaseSolidExtrude(sketch=s, depth=y_t)

        s.unsetPrimaryObject()
        p = mdb.models['Model-1'].parts['yueshuban']
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        del mdb.models['Model-1'].sketches['__profile__']

        # ----------------------------------装配---------------------------------------------------------------------------
        a = mdb.models['Model-1'].rootAssembly
        session.viewports['Viewport: 1'].setValues(displayedObject=a)
        session.viewports['Viewport: 1'].assemblyDisplay.setValues(
            optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)

        a = mdb.models['Model-1'].rootAssembly
        a.DatumCsysByDefault(CARTESIAN)
        p = mdb.models['Model-1'].parts['dianbann']
        a.Instance(name='dianbann-1', part=p, dependent=ON)
        p = mdb.models['Model-1'].parts['hexin']
        a.Instance(name='hexin-1', part=p, dependent=ON)
        p = mdb.models['Model-1'].parts['lianjieban']
        a.Instance(name='lianjieban-1', part=p, dependent=ON)
        p = mdb.models['Model-1'].parts['yueshuban']
        a.Instance(name='yueshuban-1', part=p, dependent=ON)
        p = a.instances['hexin-1']
        p.translate(vector=(500.0, 0.0, 0.0))
        p = a.instances['lianjieban-1']
        p.translate(vector=(754.5, 0.0, 0.0))
        p = a.instances['yueshuban-1']
        p.translate(vector=(839.5, 0.0, 0.0))
        session.viewports['Viewport: 1'].view.fitView()
        # 约束板约束到垫板上
        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['yueshuban-1'].faces
        f2 = a.instances['dianbann-1'].faces
        a.FaceToFace(movablePlane=f1[5], fixedPlane=f2[14], flip=ON, clearance=0.0)

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['yueshuban-1'].faces
        f2 = a.instances['dianbann-1'].faces
        a.FaceToFace(movablePlane=f1[3], fixedPlane=f2[13], flip=OFF, clearance=0.0)

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['yueshuban-1'].faces
        f2 = a.instances['dianbann-1'].faces
        a.FaceToFace(movablePlane=f1[0], fixedPlane=f2[8], flip=OFF, clearance=0.0)
        #: 实例 "yueshuban-1"  是完全约束的
        # 阵列约束版
        a1 = mdb.models['Model-1'].rootAssembly
        a1.LinearInstancePattern(instanceList=('yueshuban-1',), direction1=(1.0, 0.0,
                                                                            0.0), direction2=(0.0, 1.0, 0.0),
                                 number1=1, number2=3, spacing1=400.0,
                                 spacing2=67.0)
        # 约束阵列得到的其中一块约束板到垫板上
        a1 = mdb.models['Model-1'].rootAssembly
        f1 = a1.instances['yueshuban-1-lin-1-2'].faces
        f2 = a1.instances['dianbann-1'].faces
        a1.FaceToFace(movablePlane=f1[4], fixedPlane=f2[15], flip=ON, clearance=0.0)

        a1 = mdb.models['Model-1'].rootAssembly
        f1 = a1.instances['yueshuban-1-lin-1-2'].faces
        f2 = a1.instances['dianbann-1'].faces
        a1.FaceToFace(movablePlane=f1[0], fixedPlane=f2[8], flip=OFF, clearance=0.0)

        a1 = mdb.models['Model-1'].rootAssembly
        f1 = a1.instances['yueshuban-1-lin-1-2'].faces
        f2 = a1.instances['dianbann-1'].faces
        a1.FaceToFace(movablePlane=f1[3], fixedPlane=f2[13], flip=OFF, clearance=0.0)
        #: 实例 "yueshuban-1-lin-1-2"  是完全约束的
        # 阵列垫板
        a1 = mdb.models['Model-1'].rootAssembly
        a1.LinearInstancePattern(instanceList=('dianbann-1',), direction1=(1.0, 0.0,
                                                                           0.0), direction2=(0.0, 1.0, 0.0),
                                 number1=1, number2=2, spacing1=400.0,
                                 spacing2=67.0)
        # 约束阵列的垫板到主体上
        a1 = mdb.models['Model-1'].rootAssembly
        f1 = a1.instances['dianbann-1-lin-1-2'].faces
        f2 = a1.instances['yueshuban-1-lin-1-2'].faces
        a1.FaceToFace(movablePlane=f1[6], fixedPlane=f2[5], flip=ON, clearance=0.0)

        a1 = mdb.models['Model-1'].rootAssembly
        f1 = a1.instances['dianbann-1-lin-1-2'].faces
        f2 = a1.instances['yueshuban-1-lin-1-2'].faces
        a1.FaceToFace(movablePlane=f1[8], fixedPlane=f2[0], flip=OFF, clearance=0.0)

        a1 = mdb.models['Model-1'].rootAssembly
        f1 = a1.instances['dianbann-1-lin-1-2'].faces
        f2 = a1.instances['dianbann-1'].faces
        a1.FaceToFace(movablePlane=f1[13], fixedPlane=f2[13], flip=OFF, clearance=0.0)
        #: 实例 "dianbann-1-lin-1-2"  是完全约束的
        # 将阵列的另一块约束板约束到主体上

        a1 = mdb.models['Model-1'].rootAssembly
        f1 = a1.instances['yueshuban-1-lin-1-3'].faces
        f2 = a1.instances['dianbann-1-lin-1-2'].faces
        a1.FaceToFace(movablePlane=f1[4], fixedPlane=f2[15], flip=ON, clearance=0.0)

        a1 = mdb.models['Model-1'].rootAssembly
        f1 = a1.instances['yueshuban-1-lin-1-3'].faces
        f2 = a1.instances['dianbann-1-lin-1-2'].faces
        a1.FaceToFace(movablePlane=f1[0], fixedPlane=f2[8], flip=OFF, clearance=0.0)

        a1 = mdb.models['Model-1'].rootAssembly
        f1 = a1.instances['yueshuban-1-lin-1-3'].faces
        f2 = a1.instances['dianbann-1-lin-1-2'].faces
        a1.FaceToFace(movablePlane=f1[3], fixedPlane=f2[13], flip=OFF, clearance=0.0)
        #: 实例 "yueshuban-1-lin-1-3"  是完全约束的
        # 将约束部分合并成一个整体
        a1 = mdb.models['Model-1'].rootAssembly
        a1.InstanceFromBooleanMerge(name='hebingyuesu', instances=(
            a1.instances['dianbann-1'], a1.instances['yueshuban-1'],
            a1.instances['yueshuban-1-lin-1-2'], a1.instances['yueshuban-1-lin-1-3'],
            a1.instances['dianbann-1-lin-1-2'],), originalInstances=SUPPRESS,
                                    domain=GEOMETRY)
        # 阵列核心
        a1 = mdb.models['Model-1'].rootAssembly
        a1.LinearInstancePattern(instanceList=('hexin-1',), direction1=(1.0, 0.0,
                                                                        0.0), direction2=(0.0, 1.0, 0.0), number1=1,
                                 number2=2, spacing1=500.0,
                                 spacing2=45.0)
        #将核心1约束到主体上
        a1 = mdb.models['Model-1'].rootAssembly
        f1 = a1.instances['hexin-1'].faces
        f2 = a1.instances['hebingyuesu-1'].faces
        a1.FaceToFace(movablePlane=f1[49-(4 - k_num) * 8], fixedPlane=f2[17], flip=ON, clearance=1.0)

        a1 = mdb.models['Model-1'].rootAssembly
        f1 = a1.instances['hexin-1'].faces
        f2 = a1.instances['hebingyuesu-1'].faces
        a1.FaceToFace(movablePlane=f1[32 - (4 - k_num) * 8], fixedPlane=f2[13], flip=ON, clearance=dis)

        a1 = mdb.models['Model-1'].rootAssembly
        f1 = a1.instances['hexin-1'].faces
        f2 = a1.instances['hebingyuesu-1'].faces
        a1.FaceToFace(movablePlane=f1[37-(4 - k_num) * 8], fixedPlane=f2[7], flip=OFF, clearance=50.0)
        #: 实例 "hexin-1"  是完全约束的



        #将核心2约束到主体上
        a1 = mdb.models['Model-1'].rootAssembly
        f1 = a1.instances['hexin-1-lin-1-2'].faces
        f2 = a1.instances['hebingyuesu-1'].faces
        a1.FaceToFace(movablePlane=f1[32 - (4 - k_num) * 8], fixedPlane=f2[15], flip=ON, clearance=dis)

        a1 = mdb.models['Model-1'].rootAssembly
        f1 = a1.instances['hexin-1-lin-1-2'].faces
        f2 = a1.instances['hebingyuesu-1'].faces
        a1.FaceToFace(movablePlane=f1[41-(4 - k_num) * 8], fixedPlane=f2[1], flip=ON, clearance=1.0)

        a1 = mdb.models['Model-1'].rootAssembly
        f1 = a1.instances['hexin-1-lin-1-2'].faces
        f2 = a1.instances['hebingyuesu-1'].faces
        a1.FaceToFace(movablePlane=f1[37-(4 - k_num) * 8], fixedPlane=f2[7], flip=OFF, clearance=50.0)
        #: 实例 "hexin-1-lin-1-2"  是完全约束的


        #阵列连接板
        a = mdb.models['Model-1'].rootAssembly
        a.LinearInstancePattern(instanceList=('lianjieban-1',), direction1=(1.0, 0.0,
                                                                            0.0), direction2=(0.0, 1.0, 0.0), number1=2,
                                number2=1, spacing1=45.0,
                                spacing2=45.0)
        #将连接板1约束到主体上
        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['lianjieban-1'].faces
        f2 = a.instances['hexin-1-lin-1-2'].faces
        a.FaceToFace(movablePlane=f1[4], fixedPlane=f2[17+16-(4 - k_num) * 8], flip=ON, clearance=0.0)

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['lianjieban-1'].faces
        f2 = a.instances['hexin-1-lin-1-2'].faces
        a.FaceToFace(movablePlane=f1[1], fixedPlane=f2[20+16-(4 - k_num) * 8], flip=OFF, clearance=0.0)

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['lianjieban-1'].faces
        f2 = a.instances['hexin-1-lin-1-2'].faces
        a.FaceToFace(movablePlane=f1[2], fixedPlane=f2[21+16-(4 - k_num) * 8], flip=OFF, clearance=0.0)
        #: 实例 "lianjieban-1"  是完全约束的
        #将连接板2约束到主体上
        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['lianjieban-1-lin-2-1'].faces
        f2 = a.instances['hexin-1-lin-1-2'].faces
        a.FaceToFace(movablePlane=f1[4], fixedPlane=f2[17+16-(4 - k_num) * 8], flip=ON, clearance=0.0)

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['lianjieban-1-lin-2-1'].faces
        f2 = a.instances['hexin-1'].faces
        a.FaceToFace(movablePlane=f1[1], fixedPlane=f2[30+16-(4 - k_num) * 8], flip=OFF, clearance=0.0)

        a = mdb.models['Model-1'].rootAssembly
        f1 = a.instances['lianjieban-1-lin-2-1'].faces
        f2 = a.instances['hexin-1-lin-1-2'].faces
        a.FaceToFace(movablePlane=f1[0], fixedPlane=f2[29+16-(4 - k_num) * 8], flip=OFF, clearance=0.0)
        #: 实例 "lianjieban-1-lin-2-1"  是完全约束的

        # 合并核心


        a = mdb.models['Model-1'].rootAssembly
        a.InstanceFromBooleanMerge(name='hebinghexin', instances=(
            a.instances['hexin-1-lin-1-2'], a.instances['lianjieban-1'],
            a.instances['hexin-1'], a.instances['lianjieban-1-lin-2-1'],),
                                   keepIntersections=ON, originalInstances=SUPPRESS, domain=GEOMETRY)

        # ----------------------------------属性---------------------------------------------------------------------------
        # 复制模型
        mdb.Model(name='Model-2', objectToCopy=mdb.models['Model-1'])
        #: 模型 "Model-2" 已创建.

        # 创建约束材料
        mdb.models['Model-2'].Material(name='yueshu')
        mdb.models['Model-2'].materials['yueshu'].Elastic(table=((250000.0,
                                                                  0.27),))

        # 创建核心材料
        mdb.models['Model-2'].Material(name='hexin')
        mdb.models['Model-2'].materials['hexin'].Elastic(table=((ee,
                                                                 uuu),))
        mdb.models['Model-2'].materials['hexin'].Plastic(hardening=COMBINED,
                                                         dataType=PARAMETERS, numBackstresses=3,
                                                         table=((rr, c1, gama1,
                                                                 c2, gama2, c3, gama3),))
        mdb.models['Model-2'].materials['hexin'].plastic.CyclicHardening(parameters=ON,
                                                                         table=((rr, qq, bb),))
        # 创建约束截面
        mdb.models['Model-2'].HomogeneousSolidSection(name='YUESHU', material='yueshu',
                                                      thickness=None)
        # 创建核心截面
        mdb.models['Model-2'].HomogeneousSolidSection(name='HEXIN', material='hexin',
                                                      thickness=None)

        # 指派核心截面
        p = mdb.models['Model-2'].parts['hebinghexin']
        c = p.cells
        cells = c[0:4]
        region = regionToolset.Region(cells=cells)
        p = mdb.models['Model-2'].parts['hebinghexin']
        p.SectionAssignment(region=region, sectionName='HEXIN', offset=0.0,
                            offsetType=MIDDLE_SURFACE, offsetField='',
                            thicknessAssignment=FROM_SECTION)
        # 指派约束截面

        p = mdb.models['Model-2'].parts['hebingyuesu']
        c = p.cells
        cells = c.getSequenceFromMask(mask=('[#1 ]',), )
        region = regionToolset.Region(cells=cells)
        p = mdb.models['Model-2'].parts['hebingyuesu']
        p.SectionAssignment(region=region, sectionName='YUESHU', offset=0.0,
                            offsetType=MIDDLE_SURFACE, offsetField='',
                            thicknessAssignment=FROM_SECTION)





        # ----------------------------------网络---------------------------------------------------------------------------
        session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF,
                                                               engineeringFeatures=OFF, mesh=ON)
        session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
            meshTechnique=ON)
        # 拆分约束块
        p = mdb.models['Model-2'].parts['hebingyuesu']
        c = p.cells
        pickedCells = c.getSequenceFromMask(mask=('[#1 ]',), )
        e, v, d = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v[19], normal=e[26], cells=pickedCells)

        p = mdb.models['Model-2'].parts['hebingyuesu']
        c = p.cells
        pickedCells = c.getSequenceFromMask(mask=('[#2 ]',), )
        e1, v1, d1 = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v1[42], normal=e1[54],
                                          cells=pickedCells)

        p = mdb.models['Model-2'].parts['hebingyuesu']
        c = p.cells
        pickedCells = c.getSequenceFromMask(mask=('[#8 ]',), )
        e, v, d = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v[26], normal=e[30], cells=pickedCells)

        p = mdb.models['Model-2'].parts['hebingyuesu']
        c = p.cells
        pickedCells = c.getSequenceFromMask(mask=('[#10 ]',), )
        e1, v1, d1 = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v1[42], normal=e1[55],
                                          cells=pickedCells)

        p = mdb.models['Model-2'].parts['hebingyuesu']
        c = p.cells
        pickedCells = c.getSequenceFromMask(mask=('[#20 ]',), )
        e, v, d = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v[51], normal=e[73], cells=pickedCells)

        p = mdb.models['Model-2'].parts['hebingyuesu']
        c = p.cells
        pickedCells = c.getSequenceFromMask(mask=('[#40 ]',), )
        e1, v1, d1 = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v1[61], normal=e1[94],
                                          cells=pickedCells)

        p = mdb.models['Model-2'].parts['hebingyuesu']
        c = p.cells
        pickedCells = c.getSequenceFromMask(mask=('[#8 ]',), )
        e, v, d = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v[33], normal=e[46], cells=pickedCells)

        p = mdb.models['Model-2'].parts['hebingyuesu']
        c = p.cells
        pickedCells = c.getSequenceFromMask(mask=('[#10 ]',), )
        e1, v1, d1 = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v1[10], normal=e1[13],
                                          cells=pickedCells)

        p = mdb.models['Model-2'].parts['hebingyuesu']
        c = p.cells
        pickedCells = c.getSequenceFromMask(mask=('[#100 ]',), )
        e, v, d = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v[29], normal=e[125],
                                          cells=pickedCells)

        p = mdb.models['Model-2'].parts['hebingyuesu']
        c = p.cells
        pickedCells = c.getSequenceFromMask(mask=('[#1 ]',), )
        e1, v1, d1 = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v1[72], normal=e1[117],
                                          cells=pickedCells)

        p = mdb.models['Model-2'].parts['hebingyuesu']
        c = p.cells
        pickedCells = c.getSequenceFromMask(mask=('[#100 ]',), )
        e, v, d = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v[0], normal=e[7], cells=pickedCells)

        p = mdb.models['Model-2'].parts['hebingyuesu']
        c = p.cells
        pickedCells = c.getSequenceFromMask(mask=('[#200 ]',), )
        e, v, d = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v[21], normal=e[27], cells=pickedCells)

        p = mdb.models['Model-2'].parts['hebingyuesu']
        c = p.cells
        pickedCells = c.getSequenceFromMask(mask=('[#4000 ]',), )
        e1, v1, d1 = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v1[6], normal=e1[11],
                                          cells=pickedCells)

        p = mdb.models['Model-2'].parts['hebingyuesu']
        c = p.cells
        pickedCells = c.getSequenceFromMask(mask=('[#8000 ]',), )
        e, v, d = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v[20], normal=e[25], cells=pickedCells)

        p = mdb.models['Model-2'].parts['hebingyuesu']
        c = p.cells
        pickedCells = c.getSequenceFromMask(mask=('[#400 ]',), )
        e1, v1, d1 = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v1[45], normal=e1[83],
                                          cells=pickedCells)

        p = mdb.models['Model-2'].parts['hebingyuesu']
        c = p.cells
        pickedCells = c.getSequenceFromMask(mask=('[#4000 ]',), )
        e, v, d = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v[26], normal=e[34], cells=pickedCells)

        p = mdb.models['Model-2'].parts['hebingyuesu']
        c = p.cells
        pickedCells = c.getSequenceFromMask(mask=('[#1000 ]',), )
        e1, v1, d1 = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v1[13], normal=e1[15],
                                          cells=pickedCells)

        p = mdb.models['Model-2'].parts['hebingyuesu']
        c = p.cells
        pickedCells = c.getSequenceFromMask(mask=('[#2 ]',), )
        e, v, d = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v[65], normal=e[122],
                                          cells=pickedCells)

        # 为约束块布种
        p = mdb.models['Model-2'].parts['hebingyuesu']
        p.seedPart(size=5.0, deviationFactor=0.1, minSizeFactor=0.1)
        # 为约束块生成网格
        p = mdb.models['Model-2'].parts['hebingyuesu']
        p.generateMesh()

        #切分核心
        p = mdb.models['Model-2'].parts['hebinghexin']
        c = p.cells
        pickedCells = c.findAt(((220.0, 22.5, dis+0.2),), ((220.0, 22.5, -y_t-dis-0.2),))
        e, v, d = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v.findAt(coordinates=(-205.0, 22.5,
                                                                      dis+h_t)),
                                          normal=e.findAt(coordinates=(-238.75, 22.5, dis+h_t)),
                                          cells=pickedCells)

        p = mdb.models['Model-2'].parts['hebinghexin']
        c = p.cells
        pickedCells = c.findAt(((0.,-12.5,dis+0.2),), ((0.,-12.5,-y_t-dis-0.2),))
        e1, v1, d1 = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v1.findAt(coordinates=(-196.464466,
                                                                       13.964466, dis+h_t)),
                                          normal=e1.findAt(coordinates=(-238.75, 22.5, dis+h_t)),
                                          cells=pickedCells)

        p = mdb.models['Model-2'].parts['hebinghexin']
        c = p.cells
        pickedCells = c.findAt(((0.,-12.5,dis+0.2),), ((0.,-12.5,-y_t-dis-0.2),))
        e, v, d = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v.findAt(coordinates=(-192.928932,
                                                                      12.5, dis+h_t)),
                                          normal=e.findAt(coordinates=(-144.696699, 12.5, dis+h_t)),
                                          cells=pickedCells)

        p = mdb.models['Model-2'].parts['hebinghexin']
        c = p.cells
        pickedCells = c.findAt(((0.,-12.5,dis+0.2),), ((0.,-12.5,-y_t-dis-0.2),))
        e1, v1, d1 = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v1.findAt(coordinates=(205.0, 22.5,
                                                                       dis + h_t)),
                                          normal=e1.findAt(coordinates=(216.25, 22.5, dis+h_t)),
                                          cells=pickedCells)

        p = mdb.models['Model-2'].parts['hebinghexin']
        c = p.cells
        pickedCells = c.findAt(((0.,-12.5,dis+0.2),), ((0.,-12.5,-y_t-dis-0.2),))
        e, v, d = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v.findAt(coordinates=(196.464466,
                                                                      13.964466, dis+h_t)),
                                          normal=e.findAt(coordinates=(216.25, 22.5, dis+h_t)),
                                          cells=pickedCells)

        p = mdb.models['Model-2'].parts['hebinghexin']
        c = p.cells
        pickedCells = c.findAt(((0.,-12.5,dis+0.2),), ((0.,-12.5,-y_t-dis-0.2),))
        e1, v1, d1 = p.edges, p.vertices, p.datums
        p.PartitionCellByPlanePointNormal(point=v1.findAt(coordinates=(192.928932,
                                                                       12.5, dis+h_t)),
                                          normal=e1.findAt(coordinates=(48.232233, 12.5, dis+h_t)),
                                          cells=pickedCells)

        # 为核心布种
        p = mdb.models['Model-2'].parts['hebinghexin']
        session.viewports['Viewport: 1'].setValues(displayedObject=p)
        p = mdb.models['Model-2'].parts['hebinghexin']
        ########################################################################################################################
        p.seedPart(size=h_t / 2, deviationFactor=0.1, minSizeFactor=0.1)

        #为圆弧布种
        p = mdb.models['Model-2'].parts['hebinghexin']
        e = p.edges
        #########################################################################################
        yuanhu_edges_suoyin1 = list(range(14, 29 + (k_num-2) * 8, 2))
        ###############################################################################################
        yuanhu_edges_suoyin2 = list(range(38 + (k_num-2) * 8, 53 + (k_num-2) * 16, 2))
        yuanhu_edges_suoyin3 = list(range(116 + (k_num - 2) * 16,131 + (k_num - 2) * 24, 2))
        yuanhu_edges_suoyin4 = list(range(139 + (k_num - 2) * 24, 154 + (k_num - 2) * 32, 2))
        yuanhu_edges1 = [e[ww] for ww in yuanhu_edges_suoyin1]
        yuanhu_edges2 = [e[nn] for nn in yuanhu_edges_suoyin2]
        yuanhu_edges3 = [e[mm] for mm in yuanhu_edges_suoyin3]
        yuanhu_edges4 = [e[ll] for ll in yuanhu_edges_suoyin4]
        pickedEdges = yuanhu_edges1 + yuanhu_edges2
        p.seedEdgeBySize(edges=pickedEdges, size= h_t / 5, deviationFactor=0.1,
                         minSizeFactor=0.1, constraint=FINER)

        #核心生成网络
        #核心中性轴算法



        p = mdb.models['Model-2'].parts['hebinghexin']
        c = p.cells
        pickedRegions = c[11:12]
        p.generateMesh(regions=pickedRegions)

        p = mdb.models['Model-2'].parts['hebinghexin']
        c = p.cells
        pickedRegions = c[10:11]
        p.generateMesh(regions=pickedRegions)

        p = mdb.models['Model-2'].parts['hebinghexin']
        c = p.cells
        pickedRegions = c[15:16]
        p.generateMesh(regions=pickedRegions)

        p = mdb.models['Model-2'].parts['hebinghexin']
        c = p.cells
        pickedRegions = c[8:10]
        p.generateMesh(regions=pickedRegions)

        p = mdb.models['Model-2'].parts['hebinghexin']
        c = p.cells
        pickedRegions = c[6:8]
        p.generateMesh(regions=pickedRegions)

        p = mdb.models['Model-2'].parts['hebinghexin']
        c = p.cells
        pickedRegions = c[12:13] + c[14:15]
        p.generateMesh(regions=pickedRegions)

        p = mdb.models['Model-2'].parts['hebinghexin']
        c = p.cells
        pickedRegions = c[13:14]
        p.generateMesh(regions=pickedRegions)

        p = mdb.models['Model-2'].parts['hebinghexin']
        c = p.cells
        pickedRegions = c[3:4] + c[5:6]
        p.generateMesh(regions=pickedRegions)

        p = mdb.models['Model-2'].parts['hebinghexin']
        c = p.cells
        pickedRegions = c[0:1] + c[2:3]
        p.generateMesh(regions=pickedRegions)

        p = mdb.models['Model-2'].parts['hebinghexin']
        c = p.cells
        pickedRegions = c[1:2] + c[4:5]
        p.generateMesh(regions=pickedRegions)

        # ----------------------------------相互作用——耦合---------------------------------------------------------------------------
        # 创建参考点
        a = mdb.models['Model-2'].rootAssembly
        a.ReferencePoint(point=(-250.0, 0.0, -(y_t) / 2))

        a = mdb.models['Model-2'].rootAssembly
        a.ReferencePoint(point=(250.0, 0.0, -(y_t) / 2))

        #创建耦合1
        a = mdb.models['Model-2'].rootAssembly
        r1 = a.referencePoints
        refPoints1 = (r1[48],)
        region1 = regionToolset.Region(referencePoints=refPoints1)
        a = mdb.models['Model-2'].rootAssembly
        s1 = a.instances['hebinghexin-1'].faces
        side1Faces1 = s1.findAt(((-250.0, -15.0, 0),), ((-250.0, 7.5, -y_t-dis-0.2),),
                                ((-250.0, 7.5, dis+0.2),))
        region2 = regionToolset.Region(side1Faces=side1Faces1)
        mdb.models['Model-2'].Coupling(name='Constraint-1', controlPoint=region1,
                                       surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
                                       localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
        #创建耦合2
        a = mdb.models['Model-2'].rootAssembly
        r1 = a.referencePoints
        refPoints1 = (r1[49],)
        region1 = regionToolset.Region(referencePoints=refPoints1)
        a = mdb.models['Model-2'].rootAssembly
        s1 = a.instances['hebinghexin-1'].faces
        side1Faces1 = s1.findAt(((250.0, -7.5, 0),), ((250.0, 15.0, -y_t-dis-0.2),), ((
                                                                                        250.0, -7.5, dis+0.2),))
        region2 = regionToolset.Region(side1Faces=side1Faces1)
        mdb.models['Model-2'].Coupling(name='Constraint-2', controlPoint=region1,
                                       surface=region2, influenceRadius=WHOLE_SURFACE, couplingType=KINEMATIC,
                                       localCsys=None, u1=ON, u2=ON, u3=ON, ur1=ON, ur2=ON, ur3=ON)
        # ----------------------------------分析步-----------------------------------------------------------------
        # 创建分析步
        mdb.models['Model-2'].StaticStep(name='Step-1', previous='Initial',
                                         timePeriod=26.0, maxNumInc=100000000, stabilizationMagnitude=0.0002,
                                         stabilizationMethod=DISSIPATED_ENERGY_FRACTION,
                                         continueDampingFactors=False, adaptiveDampingRatio=0.05, initialInc=0.001,
                                         minInc=1e-08, maxInc=0.025, nlgeom=ON)
        session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
        # ----------------------------------相互作用接触-----------------------------------------------------------------
        # 创建相互作用属性
        mdb.models['Model-2'].ContactProperty('IntProp-1')
        mdb.models['Model-2'].interactionProperties['IntProp-1'].TangentialBehavior(
            formulation=PENALTY, directionality=ISOTROPIC, slipRateDependency=OFF,
            pressureDependency=OFF, temperatureDependency=OFF, dependencies=0, table=((
                                                                                          mc,),),
            shearStressLimit=None, maximumElasticSlip=FRACTION,
            fraction=0.005, elasticSlipStiffness=None)
        #: 相互作用属性 "IntProp-1" 已创建.
#创建相互作用
        a = mdb.models['Model-2'].rootAssembly
        s1 = a.instances['hebingyuesu-1'].faces
        side1Faces1 = s1[13:14] + s1[18:19] + s1[21:22] + s1[26:27] + s1[40:41] + s1[45:46] + \
                      s1[52:53] + s1[60:61] + s1[65:69] + s1[73:75] + s1[79:83] + s1[86:87] + s1[89:98] + \
                      s1[99:100] + s1[102:104] + s1[105:112]
        region1 = regionToolset.Region(side1Faces=side1Faces1)
        a = mdb.models['Model-2'].rootAssembly
        s1 = a.instances['hebinghexin-1'].faces
        side1Faces1 = s1[2:6] + s1[8:12] + s1[18:22] + s1[24:28] + s1[30:32] + s1[34:35] + \
                      s1[36:38] + s1[56+(k_num-2)*8:58+(k_num-2)*8] + s1[61+(k_num-2)*8:66+(k_num-2)*8] + \
                      s1[69+(k_num-2)*8:73+(k_num-2)*8] + s1[96+(k_num-2)*16:98+(k_num-2)*16] + \
                      s1[101+(k_num-2)*16:106+(k_num-2)*16] + s1[109+(k_num-2)*16:112+(k_num-2)*16]
        region2 = regionToolset.Region(side1Faces=side1Faces1)
        mdb.models['Model-2'].SurfaceToSurfaceContactStd(name='Int-1',
                                                         createStepName='Step-1', master=region1, slave=region2,
                                                         sliding=FINITE,
                                                         thickness=ON, interactionProperty='IntProp-1',
                                                         adjustMethod=NONE,
                                                         initialClearance=OMIT, datumAxis=None, clearanceRegion=None)
        #: 相互作用 "Int-1" 已创建.
        # ----------------------------------载荷-----------------------------------------------------------------
        # 左端固定
        a = mdb.models['Model-2'].rootAssembly
        f1 = a.instances['hebinghexin-1'].faces
        faces1 = f1.findAt(((-235.0, 15.0, -y_t-dis-h_t),), ((-235.0, -15.0,h_t+dis),), ((
                                                                                     -235.0, 15.0, dis),),
                           ((-235.0, -15.0, -y_t-dis),))
        region = regionToolset.Region(faces=faces1)
        mdb.models['Model-2'].EncastreBC(name='BC-1', createStepName='Step-1',
                                         region=region, localCsys=None)

        #右端只保留x向

        a = mdb.models['Model-2'].rootAssembly
        f1 = a.instances['hebinghexin-1'].faces
        faces1 = f1.findAt(((235.0, 15.0, h_t+dis),), ((235.0, -15.0, -y_t-dis-h_t),), ((
                                                                                   235.0, -15.0, -y_t-dis),),
                           ((235.0, -15.0, dis),))
        region = regionToolset.Region(faces=faces1)
        mdb.models['Model-2'].DisplacementBC(name='BC-2', createStepName='Step-1',
                                             region=region, u1=UNSET, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0,
                                             amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='',
                                             localCsys=None)

        #约束部分边界条件
        a = mdb.models['Model-2'].rootAssembly
        e1 = a.instances['hebingyuesu-1'].edges
        edges1 = e1[91:92] + e1[109:110] + e1[134:135] + e1[171:172]
        region = regionToolset.Region(edges=edges1)
        mdb.models['Model-2'].DisplacementBC(name='BC-3', createStepName='Step-1',
                                             region=region, u1=UNSET, u2=0.0, u3=0.0, ur1=0.0, ur2=0.0, ur3=0.0,
                                             amplitude=UNSET, fixed=OFF, distributionType=UNIFORM, fieldName='',
                                             localCsys=None)

        # 循环荷载
        mdb.models['Model-2'].TabularAmplitude(name='Amp-1', timeSpan=STEP,
                                               smooth=SOLVER_DEFAULT, data=((1.0, 0.0), (2.0, 1.67), (3.0, -1.67), (4.0,
                                                                                                                    1.67),
                                                                            (5.0, -1.67), (6.0, 1.67), (7.0, -1.67),
                                                                            (8.0, 2.5), (9.0, -2.5), (
                                                                                10.0, 2.5), (11.0, -2.5), (12.0, 2.5),
                                                                            (13.0, -2.5), (14.0, 3.33), (15.0,
                                                                                                         -3.33),
                                                                            (16.0, 3.33), (17.0, -3.33), (18.0, 3.33),
                                                                            (19.0, -3.33), (20.0,
                                                                                            5.0), (21.0, -5.0),
                                                                            (22.0, 5.0), (23.0, -5.0), (24.0, 5.0),
                                                                            (25.0, -5.0), (
                                                                                26.0, 0.0)))

        a = mdb.models['Model-2'].rootAssembly
        r1 = a.referencePoints
        refPoints1 = (r1[49],)
        region = regionToolset.Region(referencePoints=refPoints1)
        mdb.models['Model-2'].DisplacementBC(name='BC-4', createStepName='Step-1',
                                             region=region, u1=1.0, u2=UNSET, u3=UNSET, ur1=UNSET, ur2=UNSET, ur3=UNSET,
                                             amplitude='Amp-1', fixed=OFF, distributionType=UNIFORM, fieldName='',
                                             localCsys=None)

        # ----------------------------------作业-----------------------------------------------------------------
        # 创建作业
        mdb.Job(name=jobname, model='Model-2', description='', type=ANALYSIS,
                atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
                memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
                explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
                modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
                scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=12,
                numDomains=12, numGPUs=0)

        # 提交作业
        mdb.jobs[jobname].submit(consistencyChecking=OFF)
        mdb.jobs[jobname].waitForCompletion()

        # ----------------------------------后处理——导出数据---------------------------------------------------------------------------

        # 保存excel文件

        odb = openOdb(path=jobname + '.odb')
        wbkName = 'shuju{}.xls'.format(
            str(h_t) + '-' + str(dis) + '-' + str(y_t) + '-' + str(k_l) + '-' + str(k_w))  # 命名表格文件名
        wbk = xlwt.Workbook()  # 创建新的表格
        sheet = wbk.add_sheet('sheet1')  # 创建sheet1
        myAssembly = odb.rootAssembly
        frameRepository = odb.steps['Step-1'].frames
        RefPointSet = myAssembly.nodeSets['ASSEMBLY_CONSTRAINT-2_REFERENCE_POINT']
        for ii in range(len(frameRepository)):
            # 提取参考点RF1在y方向的支反力
            RForce = frameRepository[ii].fieldOutputs['RF']
            RefPointRForce = RForce.getSubset(region=RefPointSet)
            RForceValues = RefPointRForce.values
            RF_2 = RForceValues[0].data[0]
            # 提取参考点RF1的位移量
            displacement = frameRepository[ii].fieldOutputs['U']
            RefPointDisp = displacement.getSubset(region=RefPointSet)
            DispValue = RefPointDisp.values
            Disp = DispValue[0].data[0]
            # 将结果写入相应的行和列
            sheet.write(ii, 0, round(Disp, 6))
            sheet.write(ii, 1, round(RF_2, 6))
        wbk.save(wbkName)
        wbk.save('D:/abaqusmoxingshuju/pythonshuanghexin0/shuju{}.xls'
        .format(
            str(h_t) + '-' + str(dis) + '-' + str(y_t) + '-' + str(k_l) + '-' + str(k_w)))

        mdb.save()
        # 删除odb文件
        odb.close()
        time.sleep(600)
        odb_file_path = " D:/abaqusmoxingshuju/pythonshuanghexin0/hexinhou - distance - yuesuhou - Hcailiao - Ycailiao - K_num{}/".format(
            str(h_t) + '-' + str(dis) + '-' + str(y_t) + '-' + str(ee) + '-' + str(uuu)+ '-' + str(k_num)) + jobname + ".odb"
        if jobn % 4 != 0:

            # 检查文件是否存在
            if os.path.exists(odb_file_path):
                # 删除文件
                os.remove(odb_file_path)
            else:
                print('The file does not exist')






        mdb.save()
