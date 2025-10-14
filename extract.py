def extract_prest_sin_pa(cursor):

  query = """ 
    SELECT 
      p.prestacion_id,
      CONCAT(p.alumno_apellido, ", ", p.alumno_nombre) AS alumno,
      DATE_FORMAT(p.prestacion_fec_pase_activo, '%d-%m-%Y') AS fec_activacion,
      DATE_FORMAT(COALESCE(MAX(asig.asignpa_pa_fec_baja), asig.asignpa_fec1), '%d-%m-%Y') AS ultima_fecha_sin_pa,
      DATEDIFF(CURDATE(), COALESCE(MAX(asig.asignpa_pa_fec_baja), p.prestacion_fec_pase_activo)) AS dias_sin_pa,
      a.alumno_diagnostico,
      p.prestacion_escuela_nivel AS nivel,
      p.prestacion_escuela_turno AS turno,
      CONCAT(p.coordi_apellido, ", ", p.coordi_nombre) AS coordi,
      e.escuela_nombre,
      e.escuela_direccion,
      e.escuela_mail,
      e.escuela_tel_1,
      e.escuela_tel_2,
      l.localidad_nombre,
      par.partido_nombre
    FROM v_prestaciones p
    LEFT JOIN v_alumnos a
      ON p.prestacion_alumno = a.alumno_id
    LEFT JOIN v_asignaciones_pa asig 
      ON p.prestacion_id = asig.asignpa_prest
    LEFT JOIN v_escuelas e
      ON p.prestacion_escuela = e.escuela_id
    LEFT JOIN v_localidades l
      ON e.escuela_localidad = l.localidad_id
    LEFT JOIN v_partidos par
      ON l.localidad_partido = par.partido_id
    WHERE prestipo_nombre_corto != "TERAPIAS"
      AND prestacion_estado = 1
      AND prestacion_pa IS NULL
      AND prestacion_alumno != 522
    GROUP BY 
      p.prestacion_id, p.prestacion_alumno
   """
  cursor.execute(query)

  return cursor.fetchall()