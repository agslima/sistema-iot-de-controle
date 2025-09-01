#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Sistema IOT de controle de acesso com senha
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

import hashlib

senha = input()
# m  = hashlib.md5()
# m.update(senha.encode())
# m2 = m.hexdigest()
# print (m2)
h = hashlib.md5(senha.encode())
h2 = h.hexdigest()
print(h2)
