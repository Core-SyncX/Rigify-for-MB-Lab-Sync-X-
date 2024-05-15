import bpy
from mathutils import Vector
from mathutils import Color
from .variables import RIGIFYFORMBLAB_OT_var

var = RIGIFYFORMBLAB_OT_var

def is_finger(name):
    finger_names = ['thumb', 'index', 'middle', 'ring', 'pinky']
    for f in finger_names:
        if f in name:
            return True
    return False

def set_rigify_data(obj):
    arm = obj.data
    bcod = bpy.context.object.data

    for i in range(6):
        arm.rigify_colors.add()

    arm.rigify_colors[0].name = "Root"
    arm.rigify_colors[0].active = Color((0.5490, 1.0000, 1.0000))
    arm.rigify_colors[0].normal = Color((0.4353, 0.1843, 0.4157))
    arm.rigify_colors[0].select = Color((0.3137, 0.7843, 1.0000))
    arm.rigify_colors[0].standard_colors_lock = True
    arm.rigify_colors[1].name = "IK"
    arm.rigify_colors[1].active = Color((0.5490, 1.0000, 1.0000))
    arm.rigify_colors[1].normal = Color((0.6039, 0.0000, 0.0000))
    arm.rigify_colors[1].select = Color((0.3137, 0.7843, 1.0000))
    arm.rigify_colors[1].standard_colors_lock = True
    arm.rigify_colors[2].name = "Special"
    arm.rigify_colors[2].active = Color((0.5490, 1.0000, 1.0000))
    arm.rigify_colors[2].normal = Color((0.9569, 0.7882, 0.0471))
    arm.rigify_colors[2].select = Color((0.3137, 0.7843, 1.0000))
    arm.rigify_colors[2].standard_colors_lock = True
    arm.rigify_colors[3].name = "Tweak"
    arm.rigify_colors[3].active = Color((0.5490, 1.0000, 1.0000))
    arm.rigify_colors[3].normal = Color((0.0392, 0.2118, 0.5804))
    arm.rigify_colors[3].select = Color((0.3137, 0.7843, 1.0000))
    arm.rigify_colors[3].standard_colors_lock = True
    arm.rigify_colors[4].name = "FK"
    arm.rigify_colors[4].active = Color((0.5490, 1.0000, 1.0000))
    arm.rigify_colors[4].normal = Color((0.1176, 0.5686, 0.0353))
    arm.rigify_colors[4].select = Color((0.3137, 0.7843, 1.0000))
    arm.rigify_colors[4].standard_colors_lock = True
    arm.rigify_colors[5].name = "Extra"
    arm.rigify_colors[5].active = Color((0.5490, 1.0000, 1.0000))
    arm.rigify_colors[5].normal = Color((0.9686, 0.2510, 0.0941))
    arm.rigify_colors[5].select = Color((0.3137, 0.7843, 1.0000))
    arm.rigify_colors[5].standard_colors_lock = True

    bone_collections = {}

    for bcoll in list(bcod.collections):
        bcod.collections.remove(bcoll)

    def add_bone_collection(name, *, ui_row=0, ui_title='', sel_set=False, color_set_id=0):
        new_bcoll = bcod.collections.new(name)
        new_bcoll.rigify_ui_row = ui_row
        new_bcoll.rigify_ui_title = ui_title
        new_bcoll.rigify_sel_set = sel_set
        new_bcoll.rigify_color_set_id = color_set_id
        bone_collections[name] = new_bcoll

    def assign_bone_collections(pose_bone, *coll_names):
            assert not len(pose_bone.bone.collections)
            for name in coll_names:
                bone_collections[name].assign(pose_bone)

    def assign_bone_collection_refs(params, attr_name, *coll_names):
        ref_list = getattr(params, attr_name + '_coll_refs', None)
        if ref_list is not None:
            for name in coll_names:
                ref_list.add().set_collection(bone_collections[name])

    add_bone_collection('Fingers (IK)', ui_row=1, color_set_id=2)
    add_bone_collection('Fingers (Tweak)', ui_row=1, ui_title='(Tweak)', color_set_id=4)
    add_bone_collection('Torso', ui_row=2, color_set_id=3)
    add_bone_collection('Torso (Tweak)', ui_row=3, ui_title='(Tweak)', color_set_id=4)
    add_bone_collection('Arm.L (IK)', ui_row=4, color_set_id=2)
    add_bone_collection('Arm.L (FK)', ui_row=5, ui_title='(FK)', color_set_id=5)
    add_bone_collection('Arm.L (Tweak)', ui_row=6, ui_title='(Tweak)', color_set_id=4)
    add_bone_collection('Arm.R (IK)', ui_row=4, color_set_id=2)
    add_bone_collection('Arm.R (FK)', ui_row=5, ui_title='(FK)', color_set_id=5)
    add_bone_collection('Arm.R (Tweak)', ui_row=6, ui_title='(Tweak)', color_set_id=4)
    add_bone_collection('Leg.L (IK)', ui_row=7, color_set_id=2)
    add_bone_collection('Leg.L (FK)', ui_row=8, ui_title='(FK)', color_set_id=5)
    add_bone_collection('Leg.L (Tweak)', ui_row=9, ui_title='(Tweak)', color_set_id=4)
    add_bone_collection('Leg.R (IK)', ui_row=7, color_set_id=2)
    add_bone_collection('Leg.R (FK)', ui_row=8, ui_title='(FK)', color_set_id=5)
    add_bone_collection('Leg.R (Tweak)', ui_row=9, ui_title='(Tweak)', color_set_id=4)
    add_bone_collection('Muscle Arm.L', color_set_id=6)
    add_bone_collection('Muscle Arm.R', color_set_id=6)
    add_bone_collection('Muscle Leg.L', color_set_id=6)
    add_bone_collection('Muscle Leg.R', color_set_id=6)
    add_bone_collection('Muscle Torso', color_set_id=6)
    add_bone_collection('Muscle Neck', color_set_id=6)
    add_bone_collection('Root', ui_row=10, color_set_id=1)


    bones = var.fing_ik
    for i in range(len(bones)):
        pbone = obj.pose.bones[bones[i]]
        assign_bone_collections(pbone, 'Fingers (IK)')
        assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Fingers (Tweak)')

    bones = var.torso
    for i in range(len(bones)):
        pbone = obj.pose.bones[bones[i]]
        assign_bone_collections(pbone, 'Torso')
        assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Torso (Tweak)')

    bones = var.arm_l_ik
    for i in range(len(bones)):
        pbone = obj.pose.bones[bones[i]]
        assign_bone_collections(pbone, 'Arm.L (IK)')
        assign_bone_collection_refs(pbone.rigify_parameters, 'fk', 'Arm.L (FK)')
        assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Arm.L (Tweak)')

    bones = var.arm_r_ik
    for i in range(len(bones)):
        pbone = obj.pose.bones[bones[i]]
        assign_bone_collections(pbone, 'Arm.R (IK)')
        assign_bone_collection_refs(pbone.rigify_parameters, 'fk', 'Arm.R (FK)')
        assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Arm.R (Tweak)')

    bones = var.leg_l_ik
    for i in range(len(bones)):
        pbone = obj.pose.bones[bones[i]]
        assign_bone_collections(pbone, 'Leg.L (IK)')
        assign_bone_collection_refs(pbone.rigify_parameters, 'fk', 'Leg.L (FK)')
        assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Leg.L (Tweak)')

    bones = var.leg_r_ik
    for i in range(len(bones)):
        pbone = obj.pose.bones[bones[i]]
        assign_bone_collections(pbone, 'Leg.R (IK)')
        assign_bone_collection_refs(pbone.rigify_parameters, 'fk', 'Leg.R (FK)')
        assign_bone_collection_refs(pbone.rigify_parameters, 'tweak', 'Leg.R (Tweak)')


    arm.collections.active_index = 0

class RIGIFYFORMBLAB_OT_generaterig(bpy.types.Operator):
    bl_idname = "object.rigifyformblab_generaterig"
    bl_label = "Generate Rig"
    bl_description = "Generate Rigify Rig"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        is_muscle_rig = False

        rigify_rig = None
        muscle_rig = None

        muscle_parents = {}
        subtargets = {}

        mblab_mesh = None
        mblab_rig = None
        mblab_orig_bones = []
        for obj in bpy.data.objects.values():
            if 'manuellab_id' in obj.keys():
                mblab_mesh = obj
                if mblab_mesh.parent.type == 'ARMATURE':
                    mblab_rig = mblab_mesh.parent
                break

        if not mblab_mesh or not mblab_rig:
            print("Can't find mblab character. What's going on?")

        # keep a list of the original bones, minus the fingers. For some
        # reason these bones (minus the fingers) are kept in the rigify
        # rig and are not needed. I'm going to delete them at the end
        for pbone in mblab_rig.pose.bones:
            if not 'muscle' in pbone.name and not is_finger(pbone.name) and not 'root' in pbone.name:
                mblab_orig_bones.append(pbone.name)

        legacy_mode = False
        if "legacy_mode" in context.preferences.addons['rigify'].preferences:
            legacy_mode = True if context.preferences.addons[
                'rigify'].preferences['legacy_mode'] == 1 else False

        # Muscle rig?
        for bone_name in bpy.context.active_object.data.bones.keys():
            if "muscle" in bone_name:
                is_muscle_rig = True
                break

        if not is_muscle_rig:
            meta_rig = bpy.context.active_object
            bpy.context.view_layer.objects.active = meta_rig
            set_rigify_data(meta_rig)
            bpy.ops.pose.rigify_generate() 
        else:
            org_meta_rig = bpy.context.active_object

            bpy.ops.object.mode_set(mode='OBJECT')
            
            # Duplicate meta rig twice as muscle rig and meta rig (copy)
            bpy.context.view_layer.objects.active = org_meta_rig
            bpy.ops.object.duplicate()
            muscle_rig = bpy.context.active_object
            bpy.ops.object.duplicate()
            meta_rig = bpy.context.active_object

            muscle_rig.name = "TEMP_MUSCLE_RIG" + muscle_rig.name
            meta_rig.name = "TEMP_META_RIG" + meta_rig.name


            # Delete muscle and helper bones from meta rig
            bpy.ops.object.select_all(action='DESELECT')
            meta_rig.select_set(True)
            bpy.context.view_layer.objects.active = meta_rig

            bpy.ops.object.mode_set(mode='EDIT')
            meta_rig.data.layers[1] = True
            meta_rig.data.layers[2] = True
            bpy.ops.armature.select_all(action='DESELECT')
            bpy.ops.object.select_pattern(pattern="*muscle*")
            bpy.ops.object.select_pattern(pattern="*rot_helper*")
            bpy.ops.armature.delete()
            bpy.ops.object.mode_set(mode='OBJECT')


            # Start work on muscle rig
            bpy.ops.object.select_all(action='DESELECT')
            muscle_rig.select_set(True)
            bpy.context.view_layer.objects.active = muscle_rig
            bpy.ops.object.mode_set(mode='EDIT')

            # Rename muscle bones
            for name, bone in muscle_rig.data.edit_bones.items():
                if "rot_helper" in name:
                    bone.name = "MCH-" + name
                    bone.use_deform = False
                if "muscle" in name:
                    if "_H" in name or "_T" in name:
                        bone.name = "MCH-" + name
                        bone.use_deform = False
                    else:
                        bone.name = "DEF-" + name
            bpy.ops.object.mode_set(mode='OBJECT')

            # Save constraint subtargets - muscle rig
            bpy.ops.object.mode_set(mode='POSE')
            for name, bone in muscle_rig.pose.bones.items():
                if "rot_helper" in name or "muscle" in name:
                    temp_constraints = {}
                    for c_name, constraint in bone.constraints.items():
                        sub_name = constraint.subtarget
                        if "MCH" not in constraint.subtarget:
                            sub_name = "DEF-" + sub_name
                        temp_constraints[c_name] = sub_name
                    subtargets[name] = temp_constraints


            # Start editing muscle rig
            bpy.ops.object.mode_set(mode='EDIT')

            # Save the parents - muscle rig
            for name, bone in muscle_rig.data.edit_bones.items():
                if "rot_helper" in name or "muscle" in name:
                    if "MCH" not in bone.parent.name and "DEF" not in bone.parent.name:
                        legacy_parent_names = {
                            "thigh_L":"DEF-thigh.01_L", 
                            "thigh_R":"DEF-thigh.01_R", 
                            "calf_L":"DEF-calf.01_L", 
                            "calf_R":"DEF-calf.01_R", 
                            "upperarm_L":"DEF-upperarm.01_L",
                            "upperarm_R":"DEF-upperarm.01_R",
                            "lowerarm_L":"DEF-lowerarm.01_L",
                            "lowerarm_R":"DEF-lowerarm.01_R"
                            }
                        if legacy_mode:
                            if bone.parent.name in legacy_parent_names.keys():
                                parent_name = legacy_parent_names[bone.parent.name]
                            else:
                                parent_name = "DEF-" + bone.parent.name
                        else:
                            parent_name = "DEF-" + bone.parent.name
                    else:
                        parent_name = bone.parent.name
                    muscle_parents[name] = parent_name
                    

            # Unparent muscle bones - muscle rig
            for name, bone in bpy.context.active_object.data.edit_bones.items():
                if "rot_helper" in name or "muscle" in name:
                    bone.parent = None

            # Delete non-muscle bones from muscle rig
            bpy.ops.armature.select_all(action='DESELECT')
            for name, bone in muscle_rig.data.edit_bones.items():
                if not ("rot_helper" in name or "muscle" in name):
                    bone.select = True
            bpy.ops.armature.delete()

            # Move bones to layer 3 and 4
            for name, bone in muscle_rig.data.edit_bones.items():
                if ('DEF-lwrm' in name or 'DEF-tcs' in name or 'DEF-shld' in name \
                    or 'DEF-bcs' in name) and '_L' in name:
                    bone.layers[19] = True
                if ('MCH-lwrm' in name or 'MCH-tcs' in name or 'MCH-shld' in name \
                    or 'MCH-bcs' in name) and '_L' in name:
                    bone.layers[19] = True

                if ('DEF-lwrm' in name or 'DEF-tcs' in name or 'DEF-shld' in name \
                    or 'DEF-bcs' in name) and '_R' in name:
                    bone.layers[20] = True
                if ('MCH-lwrm' in name or 'MCH-tcs' in name or 'MCH-shld' in name \
                    or 'MCH-bcs' in name) and '_R' in name:
                    bone.layers[20] = True

                if ('DEF-lgs' in name or 'DEF-lwrl' in name) and '_L' in name:
                    bone.layers[21] = True
                if ('MCH-lgs' in name or 'MCH-lwrl' in name) and '_L' in name:
                    bone.layers[21] = True

                if ('DEF-lgs' in name or 'DEF-lwrl' in name) and '_R' in name:
                    bone.layers[22] = True
                if ('MCH-lgs' in name or 'MCH-lwrl' in name) and '_R' in name:
                    bone.layers[22] = True

                if 'DEF-abd' in name or 'DEF-spn' in name or 'DEF-pct' in name or \
                   'DEF-bk' in name or 'DEF-glt' in name:
                    bone.layers[23] = True
                if 'MCH-abd' in name or 'MCH-spn' in name or 'MCH-pct' in name or \
                   'MCH-bk' in name or 'MCH-glt' in name:
                    bone.layers[23] = True

                if 'DEF-nk' in name or 'MCH-nk' in name:
                    bone.layers[24] = True

            for name, bone in muscle_rig.data.edit_bones.items():
                if "MCH" in name or "DEF" in name:
                    bone.layers[0] = False
                    bone.layers[1] = False


            # Generate Rigify rig
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.select_all(action='DESELECT')
            meta_rig.select_set(True)
            bpy.context.view_layer.objects.active = meta_rig
            set_rigify_data(meta_rig)
            bpy.ops.pose.rigify_generate()
            rigify_rig = bpy.context.active_object #IF STILL TROUBLE, PLACE CODE AFTER THIS

            # Delete meta rig (copy)
            bpy.ops.object.select_all(action='DESELECT')
            meta_rig.select_set(True)
            bpy.context.view_layer.objects.active = meta_rig
            bpy.ops.object.delete(use_global=False)

            # Join muscle rig with generated Rigify rig
            bpy.ops.object.select_all(action='DESELECT')
            muscle_rig.select_set(True)
            rigify_rig.select_set(True)
            bpy.context.view_layer.objects.active = rigify_rig
            bpy.ops.object.join()

            # Re-parent and reconnect muscle bones
            bpy.ops.object.mode_set(mode='EDIT')
            for bone_name, parent_name in muscle_parents.items():

                # Re-parent bones
                rigify_rig.data.edit_bones[bone_name].parent = rigify_rig.data.edit_bones[parent_name] # BUG key "DEF-thigh_R" not found'
# ###
#                         if legacy_mode:
#                             if bone.parent.name == "calf_L":
#                                 parent_name = "DEF-calf.01_L"
#                             elif bone.parent.name == "calf_R":
#                                 parent_name = "DEF-calf.01_R"
#                             else:
#                                 parent_name = "DEF-" + bone.parent.name
#                         else:
#                             parent_name = "DEF-" + bone.parent.name
# ###
                # Reconnect muscle bones
                if "muscle" in bone_name:
                    if not ("_H" in bone_name or "_T" in bone_name):
                        rigify_rig.data.edit_bones[bone_name].use_connect = True

            # Reestablish Constraint subtargets
            bpy.ops.object.mode_set(mode='POSE')
            for bone_name, constraint in subtargets.items():
                for c_name, sub_name in constraint.items():
                    rigify_rig.pose.bones[bone_name].constraints[c_name].subtarget = sub_name
        

        rigify_rig = bpy.context.active_object

        # Fix IK pole targets
        bpy.ops.object.mode_set(mode='EDIT')
        for ext in ["_L", "_R"]:
            if legacy_mode:
                thigh_name = "DEF-thigh.02_L"
                calf_name = "DEF-calf.01_L"
            else:
                thigh_name = "DEF-thigh" + ext
                calf_name = "DEF-calf" + ext

            h = rigify_rig.data.edit_bones[thigh_name].head.copy()
            t = rigify_rig.data.edit_bones[calf_name].tail.copy()
            m = (h + t) / 2
            if legacy_mode:
                name = "knee_target.ik" + ext
            else:
                name = "thigh_ik_target" + ext
            rigify_rig.data.edit_bones[name].head.x = m[0]
            rigify_rig.data.edit_bones[name].tail.x = m[0]
            rigify_rig.data.edit_bones[name].head.z = m[2]
            rigify_rig.data.edit_bones[name].tail.z = m[2]
        bpy.ops.object.mode_set(mode='POSE')

        # Set "DEF-spine03" B-Bone handle
        bpy.context.object.data.bones["DEF-spine03"].bbone_handle_type_end = 'ABSOLUTE'
        
        # Fix custom shape scale
        for ext in ["_L", "_R"]:
            if legacy_mode:
                rigify_rig.pose.bones["hand.ik" + ext].custom_shape_scale_xyz = (2.5,2.5,2.5)
                rigify_rig.pose.bones["hand.fk" + ext].custom_shape_scale_xyz = (2.5,2.5,2.5)
            else:
                rigify_rig.pose.bones["hand_ik" + ext].custom_shape_scale_xyz = (2.5,2.5,2.5)

        if is_muscle_rig:
            # clean extra bones left behind
            # TODO: for some reason when I set the layers it results in 
            # some bones from the original rig left behind,
            # but it's a bit wonky. The names have .00X after them, because
            # they have the same name as the rigify_rig bones. I need to
            # delete those to clean up. I kept an original list of the bones.
            # Now I need to adjust this list to account for this naming
            # discrepancy. I'll go with the assumption that if there exists a
            # name like the original, but has .00X pattern appended to it,
            # then that bone should be deleted.
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.ops.object.select_all(action='DESELECT')
            rigify_rig.select_set(True)
            bpy.ops.object.mode_set(mode='EDIT')
            for bone in rigify_rig.pose.bones:
                for i in range(0, len(mblab_orig_bones)):
                    if mblab_orig_bones[i] in bone.name:
                        if '.00' in bone.name:
                            mblab_orig_bones[i] = bone.name
            bpy.ops.armature.select_all(action='DESELECT')
            for bn in mblab_orig_bones:
                bpy.ops.object.select_pattern(pattern=bn)
            bpy.ops.armature.delete()
            bpy.ops.object.mode_set(mode='OBJECT')
            bpy.context.object.display_type = 'SOLID'
            bpy.context.object.data.display_type = 'BBONE'

        # rigify_rig = bpy.context.active_object

        # rigify_rig.select_set(True)
        # bcod = bpy.context.object.data

        # def assign_bones_to_collection(bones_list, collection_index, bcod):
        #     collection = bcod.collections[collection_index]
        #     for bone_name in bones_list:
        #         collection.assign(bcod.bones[bone_name])
                
        # def unassign_bones_to_collection(bones_list, collection_index, bcod):
        #     collection = bcod.collections[collection_index]
        #     for bone_name in bones_list:
        #         collection.unassign(bcod.bones[bone_name])

        # # Assigning bones to collections
        # bone_collection = [
        #     (var.torso, 2),
        #     (var.arm_l_ik, 4),
        #     (var.arm_r_ik, 7),
        #     (var.leg_l_ik, 10),
        #     (var.leg_r_ik, 13),
        # ]
        
        
        # mbone_collection = [
        #     (var.fing_tweak, 1),
        #     (var.arm_l_fk, 5),
        #     (var.arm_l_tweak, 6),
        #     (var.arm_r_fk, 8),
        #     (var.arm_r_tweak, 9),
        #     (var.leg_l_fk, 11),
        #     (var.leg_l_tweak, 12),
        #     (var.leg_r_fk, 14),
        #     (var.leg_r_tweak, 15)
        # ]

    
        # for collection, index in mbone_collection:
        #     assign_bones_to_collection(collection, index, bcod)

        # for collection, index in bone_collection:
        #     assign_bones_to_collection(collection, index, bcod)
        
        # for collection, index in mbone_collection:
        #     unassign_bones_to_collection(collection, 0, bcod)
        #     unassign_bones_to_collection(collection, 2, bcod)
        #     unassign_bones_to_collection(collection, 4, bcod)
        #     unassign_bones_to_collection(collection, 7, bcod)
        #     unassign_bones_to_collection(collection, 10, bcod)
        #     unassign_bones_to_collection(collection, 13, bcod)

        # for collection, index in bone_collection:
        #     unassign_bones_to_collection(collection, 0, bcod)
        return {'FINISHED'}