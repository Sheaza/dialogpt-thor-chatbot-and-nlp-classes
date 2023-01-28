
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLOR HOWMANY KIND MATERIAL NUMBER OPERATE SIZEcommand : OPERATE NUMBER articlecommand : HOWMANY articleattribute : COLORattribute : MATERIALattribute : SIZEarticle : KINDarticle : attribute article'
    
_lr_action_items = {'OPERATE':([0,],[2,]),'HOWMANY':([0,],[3,]),'$end':([1,5,6,11,12,],[0,-2,-6,-1,-7,]),'NUMBER':([2,],[4,]),'KIND':([3,4,7,8,9,10,],[6,6,6,-3,-4,-5,]),'COLOR':([3,4,7,8,9,10,],[8,8,8,-3,-4,-5,]),'MATERIAL':([3,4,7,8,9,10,],[9,9,9,-3,-4,-5,]),'SIZE':([3,4,7,8,9,10,],[10,10,10,-3,-4,-5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'command':([0,],[1,]),'article':([3,4,7,],[5,11,12,]),'attribute':([3,4,7,],[7,7,7,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> command","S'",1,None,None,None),
  ('command -> OPERATE NUMBER article','command',3,'p_command_sell_buy','4.1.py',81),
  ('command -> HOWMANY article','command',2,'p_command_how_many','4.1.py',98),
  ('attribute -> COLOR','attribute',1,'p_attribute_color','4.1.py',104),
  ('attribute -> MATERIAL','attribute',1,'p_attribute_material','4.1.py',109),
  ('attribute -> SIZE','attribute',1,'p_attribute_size','4.1.py',114),
  ('article -> KIND','article',1,'p_article_kind','4.1.py',119),
  ('article -> attribute article','article',2,'p_article_attribute','4.1.py',124),
]
