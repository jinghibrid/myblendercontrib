# Orox uses Animated or MoCap walkcycles to generate footstep driven walks
# Copyright (C) 2012  Bassam Kurdali
#
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8-80 compliant>
import bpy
import bmesh

verts = [
    (-1.4485101473837858e-07, 1.7485121488571167, 1.160162521607333e-09),
    (-1.232170820236206, -0.8018090128898621, -9.610798268333554e-12),
    (1.2321710586547852, -0.8018090724945068, -9.610839901696977e-12),
    (0.6496307253837585, 0.40392011404037476, 5.315090589874671e-10),
    (-0.6496308445930481, 0.4039202332496643, 5.315090589874671e-10),
    (1.15427565574646, -0.7502495646476746, -1.3106872531754021e-10),
    (0.7676500082015991, -0.5788601040840149, -1.261416249231928e-10),
    (0.3830156624317169, -0.5037147998809814, -1.2421542960883158e-10),
    (-0.03506147861480713, -0.0008352245204150677, -1.2343892574762094e-10),
    (-0.38301560282707214, -0.5037147998809814, -1.2421542960883158e-10),
    (-0.7676499485969543, -0.5788601040840149, -1.261416249231928e-10),
    (-1.15427565574646, -0.7502496242523193, -1.3106872531754021e-10),
    (-1.106980323791504, -0.8366213440895081, -1.855140763229457e-10),
    (-1.4759737253189087, -1.0808607339859009, -1.855140763229457e-10),
    (-0.7379869222640991, 0.44660890102386475, 5.584183115914243e-10),
    (-1.6030374183628737e-07, 1.9740784168243408, 1.3023506717502187e-09),
    (0.7379868030548096, 0.4466087818145752, 5.584183115914243e-10),
    (1.4759738445281982, -1.0808607339859009, -1.855140763229457e-10),
    (1.106980323791504, -0.8366212844848633, -1.855140763229457e-10),
    (0.7379869222640991, -0.6730481386184692, -1.855140763229457e-10),
    (0.36899346113204956, -0.6009585857391357, -1.855140763229457e-10),
    (0.035062797367572784, -0.0008352245204150677, -1.2346257349804546e-10),
    (-0.3689934015274048, -0.6009585857391357, -1.855140763229457e-10),
    (-0.7379868626594543, -0.6730481386184692, -1.855140763229457e-10),
    (0.035062167793512344, -0.4710928201675415, -1.2346257349804546e-10),
    (-0.03506210818886757, -0.4710928201675415, -1.2343892574762094e-10),
    (-0.03506210818886757, -0.569651186466217, -1.855140763229457e-10),
    (0.035062167793512344, -0.569651186466217, -1.855662845606787e-10),
    (8.228234946727753e-07, 0.019788946956396103, -1.234507496228332e-10),
    (0.017532384023070335, 0.015561215579509735, -1.2345666156043933e-10),
    (-0.01752975396811962, 0.015561215579509735, -1.2344483768522707e-10),
    (0.030966991558670998, 0.0073629943653941154, -1.2346118571926468e-10),
    (-0.030965017154812813, 0.007362996228039265, -1.2344031352640172e-10)]
faces = [
    [1, 11, 12, 13], [0, 4, 14, 15], [2, 3, 16, 17], [4, 1, 13, 14],
    [3, 0, 15, 16], [5, 2, 17, 18], [6, 5, 18, 19], [7, 6, 19, 20],
    [9, 25, 26, 22], [29, 30, 28], [10, 9, 22, 23], [11, 10, 23, 12],
    [26, 25, 24, 27], [24, 7, 20, 27], [31, 32, 30, 29], [32, 31, 21, 8],
    [24, 25, 8, 21]]


def makedemesh():
    try:
        mesh = bpy.data.meshes['_automin_footSHA']
    except:
        mesh = bpy.data.meshes.new('_automin_footSHA')
        bm = bmesh.new()
        for vert in verts:
            bm.verts.new(vert)
        bm.verts.ensure_lookup_table()
        for face in faces:
            bm.faces.new([bm.verts[vert] for vert in face])
        bm.faces.ensure_lookup_table()
        bm.to_mesh(mesh)
        mesh.update()
    return mesh
