from o3seespy.command.element.base_element import ElementBase


class SimpleContact2D(ElementBase):
    """
    The SimpleContact2D Element Class
    
    This command is used to construct a SimpleContact2D element object.

    
    """
    op_type = 'SimpleContact2D'

    def __init__(self, osi, i_node, j_node, c_node, l_node, mat, g_tol, f_tol):
        """
        Initial method for SimpleContact2D

        Parameters
        ----------
        osi: o3seespy.OpenSeesInstance
        i_node: obj
            Retained nodes (-ndm 2 -ndf 2)
        j_node: obj
            Retained nodes (-ndm 2 -ndf 2)
        c_node: int
            Constrained node (-ndm 2 -ndf 2)
        l_node: int
            Lagrange multiplier node (-ndm 2 -ndf 2)
        mat: obj
            Unique integer object associated with previously-defined ndmaterial object
        g_tol: float
            Gap tolerance
        f_tol: float
            Force tolerance

        Examples
        --------
        >>> import o3seespy as o3
        >>> # Example is currently not working
        >>> osi = o3.OpenSeesInstance(ndm=2)
        >>> i_node = o3.node.Node(osi, 0.0, 0.0)
        >>> j_node = o3.node.Node(osi, 0.0, 1.0)
        >>> mat = o3.nd_material.ElasticIsotropic(osi, 1, 0.45)
        >>> o3.element.SimpleContact2D(osi, i_node=i_node, j_node=j_node, c_node=1, l_node=1, mat=mat, g_tol=1.0, f_tol=1.0)
        """
        self.osi = osi
        self.i_node = i_node
        self.j_node = j_node
        self.c_node = int(c_node)
        self.l_node = int(l_node)
        self.mat = mat
        self.g_tol = float(g_tol)
        self.f_tol = float(f_tol)
        osi.n_ele += 1
        self._tag = osi.n_ele
        self._parameters = [self.op_type, self._tag, self.i_node.tag, self.j_node.tag, self.c_node, self.l_node, self.mat.tag, self.g_tol, self.f_tol]
        self.to_process(osi)


class SimpleContact3D(ElementBase):
    """
    The SimpleContact3D Element Class
    
    This command is used to construct a SimpleContact3D element object.

    
    """
    op_type = 'SimpleContact3D'

    def __init__(self, osi, i_node, j_node, k_node, l_node, c_node, lagr_node, mat, g_tol, f_tol):
        """
        Initial method for SimpleContact3D

        Parameters
        ----------
        osi: o3seespy.OpenSeesInstance
        i_node: obj
            Retained nodes (-ndm 3 -ndf 3)
        j_node: obj
            Retained nodes (-ndm 3 -ndf 3)
        k_node: int
            Retained nodes (-ndm 3 -ndf 3)
        l_node: int
            Retained nodes (-ndm 3 -ndf 3)
        c_node: int
            Constrained node (-ndm 3 -ndf 3)
        lagr_node: int
            Lagrange multiplier node (-ndm 3 -ndf 3)
        mat: obj
            Unique integer object associated with previously-defined ndmaterial object
        g_tol: float
            Gap tolerance
        f_tol: float
            Force tolerance

        Examples
        --------
        >>> import o3seespy as o3
        >>> # Example is currently not working
        >>> osi = o3.OpenSeesInstance(ndm=2)
        >>> i_node = o3.node.Node(osi, 0.0, 0.0)
        >>> j_node = o3.node.Node(osi, 0.0, 1.0)
        >>> mat = o3.nd_material.ElasticIsotropic(osi, 1, 0.45)
        >>> o3.element.SimpleContact3D(osi, i_node=i_node, j_node=j_node, k_node=1, l_node=1, c_node=1, lagr_node=1, mat=mat, g_tol=1.0, f_tol=1.0)
        """
        self.osi = osi
        self.i_node = i_node
        self.j_node = j_node
        self.k_node = int(k_node)
        self.l_node = int(l_node)
        self.c_node = int(c_node)
        self.lagr_node = int(lagr_node)
        self.mat = mat
        self.g_tol = float(g_tol)
        self.f_tol = float(f_tol)
        osi.n_ele += 1
        self._tag = osi.n_ele
        self._parameters = [self.op_type, self._tag, self.i_node.tag, self.j_node.tag, self.k_node, self.l_node, self.c_node, self.lagr_node, self.mat.tag, self.g_tol, self.f_tol]
        self.to_process(osi)


class BeamContact2D(ElementBase):
    """
    The BeamContact2D Element Class
    
    This command is used to construct a BeamContact2D element object.

    
    """
    op_type = 'BeamContact2D'

    def __init__(self, osi, i_node, j_node, c_node, l_node, mat, width, g_tol, f_tol, c_flag):
        """
        Initial method for BeamContact2D

        Parameters
        ----------
        osi: o3seespy.OpenSeesInstance
        i_node: obj
            Retained nodes (-ndm 2 -ndf 3)
        j_node: obj
            Retained nodes (-ndm 2 -ndf 3)
        c_node: int
            Constrained node (-ndm 2 -ndf 2)
        l_node: int
            Lagrange multiplier node (-ndm 2 -ndf 2)
        mat: obj
            Unique integer object associated with previously-defined ndmaterial object
        width: float
            The width of the wall represented by the beam element in plane strain
        g_tol: float
            Gap tolerance
        f_tol: float
            Force  tolerance
        c_flag: int
            Optional initial contact flag

        Examples
        --------
        >>> import o3seespy as o3
        >>> # Example is currently not working
        >>> osi = o3.OpenSeesInstance(ndm=2)
        >>> i_node = o3.node.Node(osi, 0.0, 0.0)
        >>> j_node = o3.node.Node(osi, 0.0, 1.0)
        >>> mat = o3.nd_material.ElasticIsotropic(osi, 1, 0.45)
        >>> o3.element.BeamContact2D(osi, i_node=i_node, j_node=j_node, c_node=1, l_node=1, mat=mat, width=1.0, g_tol=1.0, f_tol=1.0, c_flag=1)
        """
        self.osi = osi
        self.i_node = i_node
        self.j_node = j_node
        self.c_node = int(c_node)
        self.l_node = int(l_node)
        self.mat = mat
        self.width = float(width)
        self.g_tol = float(g_tol)
        self.f_tol = float(f_tol)
        self.c_flag = int(c_flag)
        osi.n_ele += 1
        self._tag = osi.n_ele
        self._parameters = [self.op_type, self._tag, self.i_node.tag, self.j_node.tag, self.c_node, self.l_node, self.mat.tag, self.width, self.g_tol, self.f_tol, self.c_flag]
        self.to_process(osi)


class BeamContact3D(ElementBase):
    """
    The BeamContact3D Element Class
    
    This command is used to construct a BeamContact3D element object.

    
    """
    op_type = 'BeamContact3D'

    def __init__(self, osi, i_node, j_node, c_node, l_node, radius, crd_transf, mat, g_tol, f_tol, c_flag):
        """
        Initial method for BeamContact3D

        Parameters
        ----------
        osi: o3seespy.OpenSeesInstance
        i_node: obj
            Retained nodes (-ndm 3 -ndf 6)
        j_node: obj
            Retained nodes (-ndm 3 -ndf 6)
        c_node: int
            Constrained node (-ndm 3 -ndf 3)
        l_node: int
            Lagrange multiplier node (-ndm 3 -ndf 3)
        radius: float
            Constant radius of circular beam associated with beam element
        crd_transf: int
            Unique integer object associated with previously-defined geometrictransf object
        mat: obj
            Unique integer object associated with previously-defined ndmaterial object
        g_tol: float
            Gap tolerance
        f_tol: float
            Force tolerance
        c_flag: int
            Optional initial contact flag

        Examples
        --------
        >>> import o3seespy as o3
        >>> # Example is currently not working
        >>> osi = o3.OpenSeesInstance(ndm=2)
        >>> i_node = o3.node.Node(osi, 0.0, 0.0)
        >>> j_node = o3.node.Node(osi, 0.0, 1.0)
        >>> mat = o3.nd_material.ElasticIsotropic(osi, 1, 0.45)
        >>> o3.element.BeamContact3D(osi, i_node=i_node, j_node=j_node, c_node=1, l_node=1, radius=1.0, crd_transf=1, mat=mat, g_tol=1.0, f_tol=1.0, c_flag=1)
        """
        self.osi = osi
        self.i_node = i_node
        self.j_node = j_node
        self.c_node = int(c_node)
        self.l_node = int(l_node)
        self.radius = float(radius)
        self.crd_transf = int(crd_transf)
        self.mat = mat
        self.g_tol = float(g_tol)
        self.f_tol = float(f_tol)
        self.c_flag = int(c_flag)
        osi.n_ele += 1
        self._tag = osi.n_ele
        self._parameters = [self.op_type, self._tag, self.i_node.tag, self.j_node.tag, self.c_node, self.l_node, self.radius, self.crd_transf, self.mat.tag, self.g_tol, self.f_tol, self.c_flag]
        self.to_process(osi)


class BeamEndContact3D(ElementBase):
    """
    The BeamEndContact3D Element Class
    
    This command is used to construct a BeamEndContact3D element object.

    
    """
    op_type = 'BeamEndContact3D'

    def __init__(self, osi, i_node, j_node, c_node, l_node, radius, g_tol, f_tol, c_flag):
        """
        Initial method for BeamEndContact3D

        Parameters
        ----------
        osi: o3seespy.OpenSeesInstance
        i_node: obj
            Retained node from the beam (-ndm 3 -ndf 6)
        j_node: obj
            The remaining node on the beam element with ``inode`` (-ndm 3 -ndf 6)
        c_node: int
            Constrained node (-ndm 3 -ndf 3)
        l_node: int
            Lagrange multiplier node (-ndm 3 -ndf 3)
        radius: float
            Radius of circular beam associated with beam element
        g_tol: float
            Gap tolerance
        f_tol: float
            Force tolerance
        c_flag: float
            Optional initial contact flag

        Examples
        --------
        >>> import o3seespy as o3
        >>> # Example is currently not working
        >>> osi = o3.OpenSeesInstance(ndm=2)
        >>> i_node = o3.node.Node(osi, 0.0, 0.0)
        >>> j_node = o3.node.Node(osi, 0.0, 1.0)
        >>> o3.element.BeamEndContact3D(osi, i_node=i_node, j_node=j_node, c_node=1, l_node=1, radius=1.0, g_tol=1.0, f_tol=1.0, c_flag=1.0)
        """
        self.osi = osi
        self.i_node = i_node
        self.j_node = j_node
        self.c_node = int(c_node)
        self.l_node = int(l_node)
        self.radius = float(radius)
        self.g_tol = float(g_tol)
        self.f_tol = float(f_tol)
        self.c_flag = float(c_flag)
        osi.n_ele += 1
        self._tag = osi.n_ele
        self._parameters = [self.op_type, self._tag, self.i_node.tag, self.j_node.tag, self.c_node, self.l_node, self.radius, self.g_tol, self.f_tol, self.c_flag]
        self.to_process(osi)
