# scan_componentes.py

def scan_componentes(janela):

    print("\n" + "="*80)
    print(f"COMPONENTES DA JANELA: {janela.window_text()}")
    print("="*80)

    for ctrl in janela.descendants():
        try:
            print(
                f"Texto: {repr(ctrl.window_text()):<30} | "
                f"Classe: {ctrl.class_name():<20} | "
                f"ControlID: {ctrl.control_id()}"
            )
        except:
            pass

    print("="*80)