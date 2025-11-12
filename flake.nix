{
  description = "My data analysis project";

  inputs = {
    # 1. nixpkgs をインプットとして定義
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

    # 2. あなたの CustomPackages リポジトリをインプットとして追加
    # (★) ここで "github:Takuya-Mukai/CustomPackages" を指定します
    over-lay = {
      url = "github:Takuya-Mukai/nix-overlay";

      # (★) これが非常に重要です
      # CustomPackages が使う nixpkgs のバージョンを、
      # この Flake の nixpkgs のバージョンに強制的に合わせます。
      # これにより、依存関係の衝突を防ぎます。
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs =
    {
      self,
      nixpkgs,
      over-lay,
    }:
    let
      # サポートするシステム（アーキテクチャ）のリスト
      supportedSystems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];
      forAllSystems = f: nixpkgs.lib.genAttrs supportedSystems (system: f system);

    in
    {
      # --- 開発環境 (devShells) ---
      devShells = forAllSystems (
        system:
        let
          # このプロジェクト用の pkgs を定義（jq を追加する例）
          pkgs = import nixpkgs { inherit system; };

          # (★) CustomPackages から dataAnalysis 環境を取得
          baseDataShell = over-lay.devShells.${system}.dataAnalysis;

        in
        {
          # このリポジトリのデフォルトシェルを定義
          # default = baseDataShell;

          # (応用例) もし dataAnalysis 環境に加えて
          # このリポジトリだけで "jq" も使いたい場合
          default = baseDataShell.overrideAttrs (
            oldAttrs:
            let
              pyEnv = pkgs.python3.withPackages (ps: [ ps.openpyxl ]);
            in
            {
              buildInputs = oldAttrs.buildInputs ++ [ pyEnv ];
            }
          );
          # default = baseDataShell.overrideAttrs (oldAttrs: {
          #   #   # 既存のパッケージリスト(buildInputs)に jq を追加する
          #   buildInputs = oldAttrs.buildInputs ++ [ pkgs.python3.withPackages.openpyxl ];
          # });
        }
      );

      # (省略可) devShells.default を使う
      devShell = forAllSystems (system: self.devShells.${system}.default);
    };
}
